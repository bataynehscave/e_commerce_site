from django.db import models

# Create your models here.
class Product(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    discount_price = models.FloatField()
    image = models.CharField(max_length=200)

    def __str__(self) -> str :
        return self.title
    
class Order(models.Model):

    items = models.CharField(max_length = 3000)
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    location = models.CharField(max_length = 300)
    total = models.FloatField()

    def __str__(self) -> str:
        return self.name + ' order'
