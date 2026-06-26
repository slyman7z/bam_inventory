from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)