from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product,CartItem
from .serializers import ProductSerializer, CartItemSerializer



@api_view(['GET'])
def products_list(reqeust):
    # view to retrieve all the products
    products = Product.objects.all()

    #Serializing the products
    serializer = ProductSerializer(products, many=True)

    #to return serialized products as JSON data(responsr)
    return Response(serializer.data)



@api_view(['GET'])
def product_details(reqeust,pk):
    # view to retrieve specific product
    try:
        products = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        # If product does not exists, returns Not found
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #Serializing the product
    serializer = ProductSerializer(products)

    #to return serialized product as JSON data(responsr)
    return Response(serializer.data)



@api_view(['POST','GET'])
def get_or_add_Cart_Items(request):

    # To add the items in the Cart
    if request.method == 'POST':
        quantity = request.data.get('quantity',1)

        #to check if product_id is valid
        try:
            product = Product.objects.get(id=request.data.get('product_id'))
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        #if valid then we need to see whether the product is already in added in the cart before
        existing_item = CartItem.objects.filter(product_id=product.id).exists()

        if existing_item:
            # If the product is already in the cart, we can update the quantity
            existing_item.quantity += quantity
            existing_item.save()
            serializer = CartItemSerializer(existing_item)
            return Response(serializer.data)
        
        else:
            # If the product is not in the cart, we create a new cart item
            cart_item = CartItem.objects.create(product_id=product, quantity=quantity)
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    cartItems = CartItem.objects.all()
    serializer = CartItemSerializer(cartItems,many=True)
    return Response(serializer.data)



@api_view(['GET','DELETE'])
def remove_cart_item(request,pk):
    # First we ge the element
    try:
        cart_item = CartItem.objects.get(id = pk)
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # To delete the item only on delete request
    if request.method == 'DELETE':
        cart_item.delete()
        return Response('Item Deleted Successfully',status=status.HTTP_204_NO_CONTENT)
    
    # retrive the single item on get
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data)