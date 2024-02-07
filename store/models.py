from django.db import models
from django.urls import reverse
from tags.models import Tag

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120, null=True)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    image_url = models.URLField()
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("store:product-detail", kwargs={"id":self.id})# f"/store/{self.id}/" #
    
    def __str__(self):
        return f'{self.name}'

class Customer(models.Model):
    name = models.CharField(max_length=120, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.name}'
    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)