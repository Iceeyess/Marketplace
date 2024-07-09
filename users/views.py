from django.shortcuts import render

# Create your views here.


def login_user(request):
    """makeup login"""
    return render(request, 'login.html')


def logout_user(request):
    """makeup login"""
    return render(request, 'logout.html')