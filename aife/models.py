import uuid
from django.db import models
from django.conf import settings
from accounts.models import Customer


# CATEGORY 
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# PRODUCT
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    is_available = models.BooleanField(default=True)
    image_url = models.URLField(blank=True, null=True)
    #image = models.ImageField(upload_to='product_images/', default='product_images/default.jpg')

    
    def __str__(self):
        return self.product_name
  

# QUICK ENQUIRY
class QuickEnquiry(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry by {self.name}"
