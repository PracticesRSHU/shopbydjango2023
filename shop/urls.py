from django.urls import path
# from .views import *
# from . import views
from shop import views

app_name='shop'

urlpatterns=[
    path('about',views.about_shop),
    path('contact',views.contacts),
    path('product/<int:id>', views.product_detail,name='product_detail'),
    path('<slug:category_slug>/',views.product_list,name="product_list_by_category"),
    path('', views.product_list,name='product_list'),
]