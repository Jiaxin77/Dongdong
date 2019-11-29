from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'needs' #设置命名空间

urlpatterns = [
    path('postneeds',views.post_needs,name = 'post_needs'),
    path('getneeds',views.get_needs,name = 'get_needs'),
    path('getneedinfo',views.get_need_info,name = 'get_need_info'),
    path('getselfneeds',views.get_self_needs,name = 'get_self_needs')

]