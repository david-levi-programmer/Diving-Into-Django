from django.contrib import admin

from .models import Product, Customer, Order
# Register the data model made in 'models.py' here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)