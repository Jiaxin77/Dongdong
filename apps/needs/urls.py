from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'needs' #设置命名空间

urlpatterns = [
    path('postneeds',views.post_needs,name = 'post_needs'),#发布需求
    path('getneeds',views.get_needs,name = 'get_needs'),#需求列表
    path('getneedinfo',views.get_need_info,name = 'get_need_info'),#需求详情展开
    path('getselfneeds',views.get_self_needs,name = 'get_self_needs'),
    path('foremanGetNeed',views.foreman_get_need,name = 'foreman_get_need'),
    path('foremanNowNeed',views.foreman_now_need,name = 'foreman_now_need'),
    path('dealNeeds', views.deal_needs,name = 'deal_needs'),
    path('beginNeeds',views.begin_needs,name = 'begin_needs'),
    path('getAllNeeds',views.get_all_needs,name = 'get_all_needs')

]