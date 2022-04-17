from django.contrib import admin
from django.urls import path
from cart import views

urlpatterns = [
    path('cartdetails', views.cart_details, name='cartdetails'),
    path('add/<int:product_id>/', views.add_cart, name='addcart'),
    path('remove/<int:product_id>/', views.min_cart, name='decremant'),
    path('delete/<int:product_id>/', views.delete, name='delete')

]
