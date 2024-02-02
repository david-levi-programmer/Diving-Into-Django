from django.db import models
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    category = models.CharField(max_length=120)
    items = models.PositiveIntegerField()
    description = models.TextField(max_length=500)

    def get_absolute_url(self):
        return reverse("tags:category-listing", kwargs={"id":self.id})