from django.urls import path
# from .views import *
# from . import views
from shop import views

app_name='shop'

urlpatterns=[
    path('',views.about_shop),
    path('contact',views.contacts),
]