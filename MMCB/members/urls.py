from django.conf.urls import url
from members import views

urlpatterns = [
    url(r'^$', views.member_page, name='page'),
    url(r'^info/$', views.member_info, name='info'),
    url(r'^shoppinglist/$', views.member_shoppinglist, name='shoppinglist'),
    url(r'^shoppinglist/(?P<number>\d+)/$', views.member_order, name='order'),
    url(r'^orderstatus/(?P<number>\d+)/(?P<do>.+)/$', views.member_orderstatus, name='orderstatus'),
    url(r'^others/$', views.member_others, name='others'),
]
