from django.contrib import admin
from .models import Product, Warehouse, Category, SubCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'article', 'sub_category', 'cost_price']
    list_editable = ['sub_category']
    exclude = ['slug']
    filter_horizontal = ['warehouse']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_editable = ['name', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name']



# Register your models here.
