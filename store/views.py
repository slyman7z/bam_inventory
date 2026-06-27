from django.shortcuts import render
from .forms import CustomerForm

# Create your views here.
def customers(request):
    context = {}
    return render(request, 'customers.html', context)

def add_customer(request):
    form = CustomerForm()

    
    context = {'form': form}
    return render(request, 'add_customer.html', context)

