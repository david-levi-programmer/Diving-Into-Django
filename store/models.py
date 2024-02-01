from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    image_url = models.URLField()
