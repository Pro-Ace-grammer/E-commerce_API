from django.urls import path
from .views import *

urlpatterns = [
    # Retrieves all the products
    path('products/',products_list,name='products'),

    # Returns details of a specific product.
    path('products/<int:pk>',product_details,name='product-details'),

    # Adds a product to cart / also retrieves the cart items 
    path('cart/',get_or_add_Cart_Items,name='cart'),

    # Adds a product to cart / also retrieves the cart items 
    path('cart/<int:pk>',remove_cart_item,name='cart'),
]
