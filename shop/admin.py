from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Shop

class ShopAdmin(admin.ModelAdmin):
        list_display = ('first_name', 'last_name', 'username', 'shopkeeper_address', 'password', 're_enter_password', 'shop_category', 'city', 'local_address', 'shop_name', 'zip_code', 'country', 'country_code', 'phone_number')
       
admin.site.register(Shop,ShopAdmin)


