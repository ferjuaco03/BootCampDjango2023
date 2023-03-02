from rest_framework import serializers
from ProductApp.models import ProductOrder, Order, Product, Category,ProductCategory

class CategorySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    created_at=serializers.DateTimeField(read_only=True)
    
    def CreateCategory(self,data):
        Category.objects.create(**data)
    
    
       
    
class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    price=serializers.IntegerField()
    stock=serializers.IntegerField()
    created_at=serializers.DateTimeField(read_only=True)
    category=CategorySerializer(read_only=True, many=True)
    
    def CreateProduct(self,data):
        categories_data=data.pop('category')
        product=Product.objects.create(**data)
        for category_data in categories_data:
           category=Category.objects.get(pk=category_data['id'])
           ProductCategory.objects.create(category_id=category,product_id=product)

class ProductToOrderSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    
    
    
class ProductordersSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product_id.name')

    class Meta:
        model = ProductOrder
        fields = ('quantity', 'product_name')

    
   
class OrdersSerializer(serializers.ModelSerializer):
    products = ProductordersSerializer(source='productorder_set', many=True)
  
    class Meta:
        model = Order
        fields = ('id', 'shippingAdress','created_at','products')
    
    

    
class OrdersSerializerCreateUpdate(serializers.Serializer):
     #products = ProductordersSerializer(source='productorder_set', many=True)
   
    id=serializers.IntegerField(read_only=True)
    shippingAdress=serializers.CharField()
    created_at=serializers.DateTimeField(read_only=True)
    product=ProductToOrderSerializer(read_only=True, many=True)
    
    def CreateOrder(self,data):
        products_data=data.pop('product')
        print(products_data)
        order=Order.objects.create(**data)
        for product_data in products_data:
            product=Product.objects.get(pk=product_data['id'])
            ProductOrder.objects.create(order_id=order,
                                        product_id=product,
                                        quantity=product_data['quantity'])
    
    def UpdateOrder(self,data,pk):
        order=Order.objects.get(pk=pk)
        products_data=data.pop('product')
        print(data)
        order.shippingAdress=data['shippingAdress']
        for product_data in products_data:
            product=Product.objects.get(pk=product_data['id'])
            ProductOrder.objects.create(order_id=order,
                                        product_id=product,
                                        quantity=product_data['quantity'])
        
        order.save()
        
