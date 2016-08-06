"""MMCB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from products import views

urlpatterns = [
    url(r'^$', views.store_list, name='home'),
    # url(r'^store/', include('products.urls')),
    url(r'^shopping-cart/', include('shopping.urls', namespace='cart')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 以下適用於網頁讀取"settings.py"中的 MEDIA_URL 與 MEDIA_ROOT 所用
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
