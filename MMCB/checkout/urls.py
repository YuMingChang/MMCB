from django.conf.urls import url
from checkout import views

urlpatterns = [
    url(r'^$', views.checkout_page, name='page'),
]
