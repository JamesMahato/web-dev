import datetime
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Product(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=120)
    price = models.CharField(max_length=130)
    
    image = models.FileField(upload_to="static/image",default="default.jpg")

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name
    

    
    # @staticmethod
    # def get_product_by_id(ids):
    #     return product.objects.filter(id__in = ids)

class Order(models.Model):
    image = models.ImageField(upload_to='ecommerce/order/image')
    product = models.CharField(max_length=100,default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=13)
    date = models.DateField(default = datetime.datetime.today)
    total = models.CharField(max_length=(50), default='')

    class Meta:
        db_table = "Order"


