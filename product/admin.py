from django.contrib import admin
from product.models import Product,Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','image')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','image','product','user','quantity','price','address','phone','date')

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)