from django.db import models



class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Блюдо")
    description = models.TextField(default="без описания")

    # ship_kind = (
    #     ('salad', 'Салат'),
    #     ('soup', 'Суп'),
    #     ('main_course', 'Основное блюдо'),
    # )
    # kind = models.CharField(max_length=50, choices=ship_kind)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Продукт")

    def __str__(self):
        return self.name



class DishComponent(models.Model):
    "В данном варианте компонент блюда состоит только из одного продукта"
    name = models.CharField(max_length=100)
    # вес в килограммах
    weight = models.FloatField(default=0)

    dish = models.ForeignKey(Dish,
                             on_delete=models.SET_DEFAULT,
                             to_field = "name",
                             default="Отсутствует")

    product = models.ForeignKey(Product,
                                on_delete=models.SET_DEFAULT,
                                to_field="name",
                                default="Отсутствует")


    def __str__(self):
        return self.name



class Goods(models.Model):
    #  цена в рублях с плавающей точкой для копеек
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price_per_kg = models.FloatField()
    evaluation = models.TextField()
    permission_flag = models.BooleanField(default=True)
    product = models.ForeignKey(Product,
                                on_delete=models.SET_DEFAULT,
                                to_field="name",
                                default="Отсутствует")
    def __str__(self):
        return self.name