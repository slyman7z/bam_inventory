from django.urls import path
from . import views


urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('customer_detail/<str:pk>/', views.customer_detail, name='customer_detail'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('product_management/', views.product_management, name='product_management'),
    path('sales_management/', views.sales_management, name='sales_management'),
    path('new_order/', views.new_order, name='new_order'),
    path('create_order/', views.create_order, name='create_order'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_category/', views.add_category, name='add_category'),
    
]