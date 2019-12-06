from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'user' #设置命名空间

urlpatterns = [
    path('test',views.test,name='test'),
    path('index',views.index,name = 'index'),
    path('register',views.register,name = 'register'),
    path('login',views.login,name = 'login'),
    path('entInfoPost',views.ent_info_post,name = "ent_info_post"),
    path('entInfoGet',views.ent_info_get,name = "ent_info_get"),
    path('changePassword',views.change_password,name = "change_password"),
    path('foremanAddGroup',views.foreman_add_group,name = "foreman_add_group"),
    path('foremanShowGroup',views.forman_show_group,name = "foreman_show_group"),
    path('foremanInfoPost',views.foreman_info_post,name = "forman_info_post"),
    path('foremanInfoGet',views.foreman_info_get,name = "forman_info_get"),
    path('allManager',views.all_manager,name = "all_manager"),
    path('registerManager',views.register_manager, name = "register_manager"),
    path('getAuthEnterprise',views.get_auth_enterprise, name = "get_auth_enterprise"),
    path('postAuthResult',views.post_auth_result,name = "post_auth_result"),
    path('groupAddMember',views.group_add_member,name = "group_add_member"),
    path('groupShowMember',views.group_show_member, name = "group_show_member"),
    path('deleteManager',views.delete_manager,name = 'delete_manager')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)