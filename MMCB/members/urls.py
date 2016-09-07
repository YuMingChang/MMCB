from django.conf.urls import url
from members import views

urlpatterns = [
    url(r'^$', views.member_page, name='page'),
    url(r'^info/$', views.member_info, name='info'),
    url(r'^shoppinglist/$', views.member_shoppinglist, name='shoppinglist'),
    url(r'^others/$', views.member_others, name='others'),
]
