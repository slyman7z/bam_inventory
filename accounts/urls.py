from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_page, name='login'),
    # path('registration/', views.registration, name='registration'),
    # path('logout/', views.logout, name='logout'),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('forgot-password/', views.forgot_password, name='forgot_password'),
    # path('password-reset-confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    # path('password-reset-complete/', views.password_reset_complete, name='password_reset_complete'),
]