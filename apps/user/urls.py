from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'user' #设置命名空间

urlpatterns = [
    path('index',views.index,name = 'index'),
    path('register',views.register,name = 'register'),
    path('login',views.login,name = 'login'),
    path('entInfoPost',views.ent_info_post,name = "ent_info_post"),
    path('entInfoGet',views.ent_info_get,name = "ent_info_get"),
    path('changePassword',views.change_password,name = "change_password"),
    path('foremanAddGroup',views.foreman_add_group,name = "foreman_add_group"),
    path('foremanInfoPost',views.foreman_info_post,name = "forman_info_post"),
    path('foremanInfoGet',views.foreman_info_get,name = "forman_info_get")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)