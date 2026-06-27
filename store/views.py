from django.shortcuts import render, redirect
from .forms import CustomerForm
from . models import Customer
from django.contrib import messages

# Create your views here.
def customers(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customers.html', context)


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

