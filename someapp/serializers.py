from rest_framework.serializers import ModelSerializer
from . import models

<<<<<<< HEAD
class NumberSerializer(ModelSerializer):
    class Meta:
        model = models.Number
        fields = ['value', 'name', 'discoverer']
=======
class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ['name', 'country']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['name', 'price', 'manufacturer']
>>>>>>> a843fd4bf8dd8d9ec65f41d812ecbd6bfe41a75b
