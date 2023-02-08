from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_main_page, name='main_page'),
    path('products/', views.show_all_products, name='all_products'),
    path('products/<str:slug_product>', views.show_one_product, name='one_product'),
]