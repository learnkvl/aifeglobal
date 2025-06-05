from django.contrib import admin
from .models import Category, Product, QuickEnquiry
from accounts.models import Customer

# Customize the default admin site headers
admin.site.site_header = 'A IS FOR EVERYTHING ADMIN'
admin.site.site_title = 'A IS FOR EVERYTHING'
admin.site.index_title = 'Welcome to A IS FOR EVERYTHING'

# Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# Product admin
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',  'category','product_name', 'product_description','is_available','image_url',
    )
    list_filter = ('category', 'is_available')
    search_fields = ('product_name', 'product_description')


# QuickEnquiry admin
class QuickEnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'email', 'phone_number','message', 'created_at'
    )
    search_fields = ('name', 'email', 'phone_number')
    readonly_fields = ('created_at',)

# Register all models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(QuickEnquiry, QuickEnquiryAdmin)
