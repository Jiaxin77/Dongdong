from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'needs' #设置命名空间

urlpatterns = [
    path('postneeds',views.post_needs,name = 'post_needs'),
    path('getneeds',views.get_needs,name = 'get_needs'),
    path('getneedinfo',views.get_need_info,name = 'get_need_info'),
    path('getselfneeds',views.get_self_needs,name = 'get_self_needs'),
    path('foremanGetNeed',views.foreman_get_need,name = 'foreman_get_need'),
    path('foremanNowNeed',views.foreman_now_need,name = 'foreman_now_need'),
    path('dealNeeds', views.deal_needs,name = 'deal_needs'),
    path('beginNeeds',views.begin_needs,name = 'begin_needs')

]