from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requests):
  return render(requests,'shop/index.html')

def register(requests):
  return render(requests,'shop/index.html')

def login(requests):
  return render(requests,'shop/index.html')

def cart(requests):
  return render(requests,'shop/index.html')

def wishlist(requests):
  return render(requests,'shop/index.html')

def about(requests):
  return HttpResponse('about')
  # return render(requests,'shop/index.html')

def contact(requests):
  return HttpResponse('contact')
  # return render(requests,'shop/index.html')

def productview(requests):
  return HttpResponse('productview')
  # return render(requests,'shop/index.html')

def checkout(requests):
  return HttpResponse('checkout')
  # return render(requests,'shop/index.html')

def tracker(requests):
  return HttpResponse('tracker')
  # return render(requests,'shop/index.html')

def search(requests):
  return HttpResponse('search')
  # return render(requests,'shop/index.html')
