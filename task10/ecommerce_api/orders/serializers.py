from decimal import Decimal

from django.db import transaction
from rest_framework import serializers

from products.models import Product
from .models import Order, OrderItem


class OrderItemInputSerializer(serializers.Serializer):

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )

    quantity = serializers.IntegerField(min_value=1)


class OrderItemReadSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source='product.name',
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'product_name',
            'quantity',
            'price'
        ]


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemInputSerializer(
        many=True,
        write_only=True
    )

    order_items = OrderItemReadSerializer(
        source='items',
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'items',
            'order_items',
            'status',
            'total_price',
            'created_at'
        ]

        read_only_fields = [
            'id',
            'user',
            'status',
            'total_price',
            'created_at'
        ]

    def validate_items(self, value):

        if not value:
            raise serializers.ValidationError(
                "Order must contain at least one product."
            )

        product_ids = [item['product'].id for item in value]

        if len(product_ids) != len(set(product_ids)):
            raise serializers.ValidationError(
                "Duplicate products are not allowed."
            )

        return value

    @transaction.atomic
    def create(self, validated_data):

        items_data = validated_data.pop('items')

        order = Order.objects.create(
            user=self.context['request'].user
        )

        total = Decimal('0.00')

        for item in items_data:

            product = Product.objects.select_for_update().get(
                pk=item['product'].pk
            )

            quantity = item['quantity']

            if product.stock < quantity:
                raise serializers.ValidationError(
                    f"Insufficient stock for {product.name}."
                )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

            product.stock -= quantity

            product.save(update_fields=['stock'])

            total += product.price * quantity

        order.total_price = total

        order.save(update_fields=['total_price'])

        return order