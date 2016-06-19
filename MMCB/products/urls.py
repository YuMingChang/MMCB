from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.store_list, name='store_list'),
    url(r'^add/$', views.product_add, name='product_add'),
    url(r'^edit/$', views.product_edit, name='product_edit'),
    url(r'^delete/$', views.product_delete, name='product_delete'),
]
