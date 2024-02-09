from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .forms import OrderForm, CreateUserForm
from .serializers import ProductSerializer

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

def registration_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account successfully created for ' + user + '!')
                return redirect('login')

        context = {'form':form}
        return render(request, "store/accounts/register.html", context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username and/or password is wrong.')

        context = {}
        return render(request, "store/accounts/login.html", context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home_view(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered_orders = orders.filter(status="Delivered").count()
    orders_pending = orders.filter(status="Pending").count()

    context = {'orders':orders, 'customers':customers,
               'total_orders':total_orders, 'delivered':delivered_orders,
               'pending':orders_pending}
    
    return render(request, "store/accounts/dashboard.html", context)

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