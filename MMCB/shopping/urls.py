from django.conf.urls import url
from shopping import views

urlpatterns = [
    url(r'^add/$', views.add, name='shopping-cart-add'),
    url(r'^remove/$', views.remove, name='shopping-cart-remove'),
    url(r'^show/$', views.show, name='shopping-cart-show'),
]
