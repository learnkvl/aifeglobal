from django.contrib import admin
from .models import Customer

# Customize the default admin site headers
admin.site.site_header = 'A IS FOR EVERYTHING ADMIN'
admin.site.site_title = 'A IS FOR EVERYTHING'
admin.site.index_title = 'Welcome to A IS FOR EVERYTHING'

# ModelAdmin configuration
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'phone_number',
        'address_line_1', 'address_line_2', 'city', 
        'state', 'country', 'date_of_birth', 'gender',
    )

# Register the model with the default admin site
admin.site.register(Customer, CustomerProfileAdmin)
