from django.db import models

<<<<<<< HEAD
class Number(models.Model):
    value = models.FloatField()
    name = models.CharField(max_length=255)
    discoverer = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}: {self.value}"
=======
class Manufacturer(models.Model):
    name = models.CharField("Название", max_length=255)
    country = models.CharField("Страна", max_length=255)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    price = models.DecimalField("Цена", max_digits=1000, decimal_places=2)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return f"{self.name}"


>>>>>>> a843fd4bf8dd8d9ec65f41d812ecbd6bfe41a75b
