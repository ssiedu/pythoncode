from . import  views
from django.conf.urls import  url

app_name = 'basic_app'

urlpatterns =[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^notice_list/$', views.NoticeListView.as_view(), name='noticelist'),
    url(r'^(?P<pk>\d+)/$', views.NoticeDetailView.as_view(), name = 'detail'),
    #url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
]