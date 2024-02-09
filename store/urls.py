from django.urls import path

from .views import *

app_name = 'store'
urlpatterns = [
    path("accounts/dashboard", home_view, name="home"),
    path("accounts/login/", login_view, name='login'),
    path("accounts/logout/", logout_view, name='logout'),
    path("accounts/register/", registration_view, name='register'),

    path("products/", index_view, name="products"),
    path("products/<int:id>/", dynamic_product_view, name='product-detail'),

]