from django.urls import path

from .views import index_view, dynamic_product_view

app_name = 'store'
urlpatterns = [
    path("<int:id>/", dynamic_product_view, name='product-detail'),
    path("", index_view)
]