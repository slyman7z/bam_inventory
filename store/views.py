from django.shortcuts import render, redirect
from .forms import CustomerForm
from . models import Customer, Category, Product
from django.contrib import messages
import logging
from django.db.models import Q
from django.http import JsonResponse


logger = logging.getLogger(__name__)


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
        form = CustomerForm() 

    context = {'form': form}
    return render(request, 'add_customer.html', context)

def product_management(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'product_management.html', context)

def add_product(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            price = request.POST.get('price')
            category_id = request.POST.get('category')
            description = request.POST.get('description')
            image = request.FILES.get('image')

            category = Category.objects.get(id=category_id)

            Product.objects.create(
                name=name,
                price=price,
                category=category,
                description=description,
                image=image
            )

            messages.success(
                request,
                'Product record submitted successfully!'
            )
            return redirect('add_product')

        except Exception as e:
            logger.exception("Error creating product")
            messages.error(request, f'Error: {e}')

    context = {
        'categories': categories
    }

    return render(request, 'add_product.html', context)

def add_category(request):
    if request.method == 'POST':

        try:
            name = request.POST.get('name')
            description = request.POST.get('description')

            Category.objects.create(
                name=name,
                description=description
            )

            messages.success(
                request,
                'Category record submitted successfully!'
            )
            return redirect('add_category')

        except Exception as e:
            logger.exception("Error creating category")
            messages.error(request, f'Error: {e}')

    context = {}
    return render(request, 'add_category.html', context)

def sales_management(request):
    context = {}
    return render(request, 'sales_management.html', context)


def add_order(request):
    search_query = request.GET.get('search_query', '').strip()
    
    if search_query:
        customers = Customer.objects.filter(
            Q(name__icontains=search_query) |
            Q(phone1__icontains=search_query) |
            Q(city__icontains=search_query)
        ).distinct()
    else:
        customers = Customer.objects.none()

    # Check if request expects JSON (AJAX)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = list(customers.values('id', 'name', 'phone1', 'email'))
        return JsonResponse({'customers': data}, safe=False)

    return render(request, 'add_order.html', {'customers': customers, 'search_query': search_query})

