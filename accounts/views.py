from django.shortcuts import render, redirect
from django.contrib import messages, auth



# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')



        
        # Basic validation
        if not email or not password:
            messages.error(request, 'Please provide both email and password.')
            return render(request, 'login.html')
        
        user = auth.authenticate(request, email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')  
        
    return render(request, 'login.html')



