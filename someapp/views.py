<<<<<<< HEAD
import random
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Number
from .serializers import NumberSerializer

class NumberViewSet(ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

    @action(methods=['GET'], detail=False, url_path='random')
    def random_number(self, request):
        min_val = int(request.query_params.get('min', 0))
        max_val = int(request.query_params.get('max', 100))
        
        result = random.randint(min_val, max_val)
        return Response({'random_number': result})
=======
from rest_framework.viewsets import ModelViewSet
from .models import Manufacturer, Product
from .serializers import ManufacturerSerializer, ProductSerializer

class ManufacturerViewset(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
>>>>>>> a843fd4bf8dd8d9ec65f41d812ecbd6bfe41a75b
