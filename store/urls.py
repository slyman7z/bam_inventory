from django.urls import path
from . import views


urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('customer_detail/<str:pk>/', views.customer_detail, name='customer_detail'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('product_management/', views.product_management, name='product_management'),
    path('sales_management/', views.sales_management, name='sales_management'),
    path('new_order/', views.new_order, name='new_order'),
    path('create_order/<str:pk>/', views.create_order, name='create_order'),
    path('add-order/<int:pk>/<uuid:order_id>/', views.add_order, name='add_order'),
    path('apply-discount/<int:pk>/<uuid:order_id>/', views.apply_discount, name='apply_discount'),

    path('customer/<int:pk>/order/<uuid:order_id>/item/<int:item_id>/increase/', views.increase_order_quantity, name='increase_order_quantity'),
    path('customer/<int:pk>/order/<uuid:order_id>/item/<int:item_id>/decrease/', views.decrease_order_quantity, name='decrease_order_quantity'),
    path('customer/<int:pk>/order/<uuid:order_id>/item/<int:item_id>/remove/', views.remove_order_item, name='remove_order_item'),

    path('add_product/', views.add_product, name='add_product'),
    path('add_category/', views.add_category, name='add_category'),
    
]