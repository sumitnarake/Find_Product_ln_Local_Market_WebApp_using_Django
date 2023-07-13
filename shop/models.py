from django.db import models

class Shop(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    shopkeeper_address = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    re_enter_password = models.CharField(max_length=128)
    shop_category = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    local_address = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50,default='india')
    country_code = models.CharField(max_length=10,default=91)
    phone_number = models.CharField(max_length=20)

    def _str_(self):
        return self.shop_name
