from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    image_url = models.URLField()
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("store:product-detail", kwargs={"id":self.id})# f"/store/{self.id}/" #
