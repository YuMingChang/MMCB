from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from posts import views

urlpatterns = [
    url(r'^$', views.post_list, name='list'),                           # READ(Retreive)
    url(r'^create/$', views.post_create, name='create'),                # CREATE(Create Prodcut)
    url(r'^add_detail/$', views.post_add_detail, name='add_detail'),    # CREATE(Add Detail)
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),      # UPDATE
    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='delete'),    # DELETE
    url(r'^meta/$', views.meta, name='meta'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 以下適用於網頁讀取"settings.py"中的 MEDIA_URL 與 MEDIA_ROOT 所用
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
