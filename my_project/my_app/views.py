from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello Its Working")

# def simple_view(request):
#     return HttpResponse("Simple View inside my_app")

def simple_view(request):
    return render(request,'my_app/example1.html')