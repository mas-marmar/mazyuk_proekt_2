from rest_framework.viewsets import ModelViewSet
from .models import Manufacturer, Product
from .serializers import ManufacturerSerializer, ProductSerializer

class ManufacturerViewset(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
