from django.db import transaction
from django.db.models import F

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from products.models import Product

from .models import Order
from .serializers import OrderSerializer
from .permissions import IsOrderOwner


class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer

    permission_classes = [
        IsAuthenticated,
        IsOrderOwner
    ]

    def get_queryset(self):

        return Order.objects.filter(
            user=self.request.user
        ).prefetch_related(
            'items__product'
        ).order_by('-created_at')

    @action(
        detail=True,
        methods=['post'],
        url_path='cancel'
    )
    @transaction.atomic
    def cancel(self, request, pk=None):

        order = self.get_object()

        if order.status != 'Pending':

            return Response(
                {'error': 'Only pending orders can be cancelled.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        for item in order.items.all():

            Product.objects.filter(
                id=item.product_id
            ).update(
                stock=F('stock') + item.quantity
            )

        order.status = 'Cancelled'

        order.save(update_fields=['status', 'updated_at'])

        return Response({
            'message': 'Order cancelled successfully.',
            'order_id': order.id,
            'status': order.status
        })