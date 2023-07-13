from django.db import models

class Product(models.Model):
    shop_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default="others")
    product_name = models.CharField(max_length=200)
    username =models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_availability = models.CharField(max_length=200,default="Not in stock")
    local_address = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product_images/', default=None)

    def __str__(self):
        return self.product_name


    

  

