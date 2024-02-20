from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.ImageField(default='default/default.jpg',upload_to='uploads/')
    # If user doesn't upload image then the default image will be displayed
    

class CartItem(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)