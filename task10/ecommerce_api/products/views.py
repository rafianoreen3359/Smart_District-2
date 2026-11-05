from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('-created_at')

    serializer_class = ProductSerializer

    filterset_fields = ['category', 'price']

    search_fields = ['name', 'description', 'category']

    ordering_fields = ['price', 'created_at', 'name']

    def get_permissions(self):

        if self.action in ['list', 'retrieve']:
            return []

        return [IsAdminUser()]