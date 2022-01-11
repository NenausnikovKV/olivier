from django.contrib import admin

# Register your models here.
from .models import DishComponent, Goods, Product, Dish

admin.site.register(DishComponent)
admin.site.register(Goods)
admin.site.register(Product)
admin.site.register(Dish)
