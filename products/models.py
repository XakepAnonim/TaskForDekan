from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
    description = models.TextField(verbose_name='Комментарий')
