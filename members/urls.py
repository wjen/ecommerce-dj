from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
urlpatterns = [
    # stops authenticated user from going back to login page
    path('', auth_views.LoginView.as_view(
        redirect_authenticated_user=True), name='login'),
    path('register/', views.register, name='register'),
    path('change-password/', views.PasswordsChangeView.as_view(), name='change-password'),
]