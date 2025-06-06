from django.shortcuts import render
from .models import Category

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def category_product_list(request):
    categories = Category.objects.prefetch_related('product_set').all()
    return render(request, 'category_product_list.html', {'categories': categories})
