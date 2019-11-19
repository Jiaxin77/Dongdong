
from django.urls import path
from . import views

app_name = 'user' #设置命名空间

urlpatterns = [
    path('register',views.register,name = 'register'),
    path('login',views.login,name = 'login')
]