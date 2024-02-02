from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index_view(request, *args, **kwargs):
    item_list = Product.objects.all()
    item_info = {
        'object_list': item_list
    }
    return render(request, "index.html", item_info)

def dynamic_product_view(request, product_id):
    obj = Product.objects.get(id=product_id)
    context = {
        "object": obj
    }
    return render(request, "product_page.html", context)
