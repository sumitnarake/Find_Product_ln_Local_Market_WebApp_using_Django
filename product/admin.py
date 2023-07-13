from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('shop_name','city','product_name', 'username' , 'product_price', 'product_availability','local_address', 'product_image')

admin.site.register(Product, ProductAdmin)


