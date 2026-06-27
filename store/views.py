from django.shortcuts import render, redirect
from .forms import CustomerForm
from . models import Customer
from django.contrib import messages

# Create your views here.
def customers(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customers.html', context)

def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'customer': customer}
    return render(request, 'customer_detail.html', context)


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer record submitted successfully !!!')
            return redirect('customers') 
    else:
        form = CustomerForm() # 👈 Only instantiate an empty form on GET requests

    context = {'form': form}
    return render(request, 'add_customer.html', context)

def product_management(request):
    context = {}
    return render(request, 'product_management.html', context)

def add_product(request):
    context = {}
    return render(request, 'add_product.html', context)

def add_category(request):
    context = {}
    return render(request, 'add_category.html', context)