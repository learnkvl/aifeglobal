from django.urls import path
from .views import category_product_list
#from .views import home, about, blog, contact

urlpatterns = [
    # path('', home, name='home'),
    # path('about/', about, name='about'),
    # path('blog/', blog, name='blog'),
    # path('contact/', contact, name='contact'),
    path('products/', category_product_list, name='category_product_list'),
]


