from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from ProductApp.serializers import ProductSerializer, OrdersSerializer, CategorySerializer, ProductordersSerializer
from ProductApp.serializers import OrdersSerializerCreateUpdate
from ProductApp.models import Product, Order, ProductOrder,Category

@api_view(['GET','POST'])
def products(request):
    if request.method == 'GET':
        products=Product.objects.all()
        serializer_products=ProductSerializer(products, many=True)
        return Response(serializer_products.data)
    else:
        serializer_product=ProductSerializer(request.data)
        serializer_product.CreateProduct(request.data)   
        return Response(serializer_product.data)
    
    
@api_view(['GET','PUT', 'DELETE'])           
def product_detail(request, pk):
    
    product=Product.objects.get(pk=pk) 
    
    if request.method =='PUT':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            product.stock=request.data['stock'] 
            product.price=request.data['price']
            product.name=request.data['name']
            product.save()   
        serializer_product=ProductSerializer(product)
        return Response(serializer_product.data)
    elif request.method == 'DELETE':
         product.delete()
         return Response()
         
    elif request.method == 'GET':
        serializer_product=ProductSerializer(product)
        return Response(serializer_product.data)        



@api_view(['GET','POST'])
def Orders(request):
    if request.method == 'GET':
        ProductOrders=Order.objects.all()
        serializer_orders=OrdersSerializer(ProductOrders, many=True)
        return Response(serializer_orders.data)
    elif request.method == 'POST':
        serializer_order=OrdersSerializerCreateUpdate(request.data)
        serializer_order.CreateOrder(request.data)   
        return Response()

@api_view(['GET','PUT', 'DELETE'])           
def order_detail(request, pk):
    
    order=Order.objects.get(pk=pk) 
    
    if request.method =='PUT':
        serializer_order=OrdersSerializerCreateUpdate(data=request.data)
        if serializer_order.is_valid():
            serializer_order.UpdateOrder(request.data,pk)
            return Response()
    elif request.method == 'DELETE':
         order.delete()
         return Response()
         
    elif request.method == 'GET':
        serializer_order=OrdersSerializer(order)
        return Response(serializer_order.data)        

        

@api_view(['GET','POST'])
def Categories(request):
    if request.method == 'GET':
        categories=Category.objects.all()
        serializer_categories=CategorySerializer(categories, many=True)
        return Response(serializer_categories.data)
    elif request.method == 'POST':
        serializer_category=CategorySerializer(request.data)
        serializer_category.CreateCategory(request.data)   
        return Response()
    
@api_view(['GET','PUT', 'DELETE'])           
def categorie_detail(request, pk):
    
    categorie=Category.objects.get(pk=pk) 
    
    if request.method =='PUT':
        serializer_categorie=CategorySerializer(data=request.data)
        if serializer_categorie.is_valid():
            categorie.name=request.data['name']
            categorie.description=request.data['description']
            categorie.save()
            return Response()
    elif request.method == 'DELETE':
         categorie.delete()
         return Response()
         
    elif request.method == 'GET':
        serializer_categorie=CategorySerializer(categorie)
        return Response(serializer_categorie.data)        
