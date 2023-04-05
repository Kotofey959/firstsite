from django.urls import path
from .views import *

urlpatterns = [
    path('', MarketHome.as_view(), name='home'),
    path('category/<slug:category_slug>/<slug:product_slug>/<int:product_id>/', ProductView.as_view(), name='product'),
    path('category/<slug:category_slug>/', CategoryView.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', login, name='login'),
    path('cart/', cart_detail, name='cart'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('order_create/', order_create, name='order_create')
]
