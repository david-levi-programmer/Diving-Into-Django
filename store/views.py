from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def index_view(request, *args, **kwargs):
    item_list = Product.objects.all()
    item_info = {
        'object_list': item_list
    }
    return render(request, "store/index.html", item_info)

def dynamic_product_view(request, product_id):
    obj = get_object_or_404(Product, id=product_id)
    context = {
        "object": obj
    }
    return render(request, "store/product_page.html", context)
