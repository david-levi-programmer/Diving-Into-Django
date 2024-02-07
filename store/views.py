from django.shortcuts import render, get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# v Views for regular HTML templates
# def index_view(request, *args, **kwargs):
    # item_list = Product.objects.all()
    # item_info = {
        # 'object_list': item_list
    # }
    # return render(request, "store/index.html", item_info)

# def dynamic_product_view(request, product_id):
    # obj = get_object_or_404(Product, id=product_id)
    # context = {
        # "object": obj
    # }
    # return render(request, "store/product_page.html", context)

# v Views for Django REST Framework
@api_view(['GET', 'POST'])
def index_view(request, format=None):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def dynamic_product_view(request, id, format=None):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)