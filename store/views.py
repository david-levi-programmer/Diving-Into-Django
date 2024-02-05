from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# def index_view(request, *args, **kwargs):
    # item_list = Product.objects.all()
    # item_info = {
        # 'object_list': item_list
    # }
    # return render(request, "store/index.html", item_info)

@api_view('GET', 'POST')
def index_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse({'drinks':serializer.data})
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

def dynamic_product_view(request, product_id):
    obj = get_object_or_404(Product, id=product_id)
    context = {
        "object": obj
    }
    return render(request, "store/product_page.html", context)
