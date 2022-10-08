from urllib import request
from django.http import HttpResponse

def homes_view(request):
    return HttpResponse("Home_view in views py")


def login_view(request):
    return HttpResponse ("inside login_view")

def add_to_cart(request):
    return HttpResponse("Inside cart_view")
