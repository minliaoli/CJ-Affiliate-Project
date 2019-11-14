from .pyrebase_settings import db
from django.shortcuts import render

def get_products(request):
    products = db.child("products").get()
    return render(request, 'frontend/index.html', {'products': products.val()})
    
