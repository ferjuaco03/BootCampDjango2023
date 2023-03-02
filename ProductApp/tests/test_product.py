
# Django
from django.test import TestCase
from django.urls import reverse, resolve

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from ProductApp.models import Product, Category,ProductCategory,Order,ProductOrder


class ProductTestCase(TestCase):
    
    def setUp(self):
    
        self.category_1 = { 
                         "name": "Computadores",
                         "description": "Computadores de diferentes marcas"
                        }
        self.category_2 = { 
                         "name": "Ropa",
                         "description": "prendasde vestir de diferentes marcas"
                        }
        self.product = { 
                            "name": "Camiseta roja",
                            "description": "Camiseta de color rojo de algodon",
                            "price":100,
                            "stock":50,
                            "category":[]
                        }
        
        self.product_1 = { 
                            "name": "Hoodie rojo",
                            "description": "Hoodie de color rojo de algodon",
                            "price":100,
                            "stock":50,
                            
                        }
        
        self.product_2 = { 
                            "name": "Televisor LG 40Pulg ",
                            "description": "Televisor lg 40pulg 4K",
                            "price":100,
                            "stock":50,
                            
                         }
        self.order = { 
                            "shippingAdress": "Adress 1",
                            "product":[]
                        }
        
        self.order_1 = { 
                            "shippingAdress": "Adress 2",
                            
                        }
        self.order_2 = { 
                            "shippingAdress": "Adress 3",
                            
                        }
        
 
    def test_get_url_is_resolved(self):
            self.url=reverse('categories')
        
        
    def test_create_category(self):
        self.url=reverse('categories')
        client = APIClient()
        response = client.post(
            self.url, 
            self.category_1,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_categories(self):
        self.url=reverse('categories')
        client = APIClient()
        Category.objects.create(**self.category_1)
        Category.objects.create(**self.category_2)
        
        response = client.get(self.url)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)
        
        
    def test_create_product(self):
            self.url=reverse('products')
            client = APIClient()
            response = client.post(
                self.url, 
                self.product,
                format='json'
            )
            result = json.loads(response.content)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_products(self):
        self.url=reverse('products')
        client = APIClient()
        cat1=Category.objects.create(**self.category_1)
        cat2=Category.objects.create(**self.category_2)
        pro1=Product.objects.create(**self.product_1)
        pro2=Product.objects.create(**self.product_2)
        ProductCategory.objects.create(category_id=cat1,product_id=pro1)
        ProductCategory.objects.create(category_id=cat2,product_id=pro2)
        response = client.get(self.url)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)
    
    def test_create_order(self):
        self.url=reverse('orders')
        client = APIClient()
        response = client.post(
            self.url, 
            self.order,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_products(self):
        self.url=reverse('orders')
        client = APIClient()
        order1=Order.objects.create(**self.order_1)
        order2=Order.objects.create(**self.order_2)
        pro1=Product.objects.create(**self.product_1)
        pro2=Product.objects.create(**self.product_2)
        ProductOrder.objects.create(order_id=order1,product_id=pro1,quantity=10)
        ProductOrder.objects.create(order_id=order2,product_id=pro2,quantity=5)
        response = client.get(self.url)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)
    