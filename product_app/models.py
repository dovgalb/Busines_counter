from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    article = models.CharField(max_length=100, verbose_name='Артикул', unique=True)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)
    characteristics = models.TextField(verbose_name='Описание')
    cost_price = models.IntegerField(verbose_name='Себестоимость')
    warehouse = models.ManyToManyField('Warehouse', verbose_name='Склад')
    count = models.IntegerField(verbose_name='Кол-во', default=0)
    slug = models.SlugField(default='', null=False, db_index=True, blank=True)

    def __str__(self):
        return f'название:{self.name}, цена{self.cost_price}'

    def save(self, *args, **kwargs):
        self.slug=slugify(f'{self.article}')
        super(Product, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one_product', args=[self.slug])


class Warehouse(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Подкатегория')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}|{self.category}'



# Create your models here.
