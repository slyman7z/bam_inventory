from django.urls import path
from . import views


urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('customer_detail/<str:pk>/', views.customer_detail, name='customer_detail'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('product_management/', views.product_management, name='product_management'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_category/', views.add_category, name='add_category'),
]