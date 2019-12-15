from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'order' #设置命名空间

urlpatterns = [
    path('getOrders', views.get_orders, name ='get_orders'),
    path('payForOrders', views.pay_for_orders, name ='pay_for_orders'),
    path('getOrderInfo',views.get_order_info, name='getOrderInfo'),
    path('getAllOrders',views.get_all_orders,name='getAllOrders')
]