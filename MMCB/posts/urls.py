from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from posts import views

urlpatterns = [
    url(r'^$', views.post_page, name='page'),
    url(r'^products/', include([
        # READ(Retreive)
        url(r'^$', views.post_products_list, name='list'),

        # CREATE(Prodcut)
        url(r'^create/$', views.post_product_add, name='create'),

        # CREATE(Detail)
        url(r'^add_detail/$', views.post_detail_add, name='add_detail'),
        url(r'^add_detail/(?P<id>\d+)/$', views.post_detail_add, name='add_detail'),

        # UPDATE
        url(r'^edit/(?P<id>\d+)/$', views.post_product_update, name='update'),

        # DELETE
        url(r'^delete/(?P<id>\d+)/$', views.post_product_delete, name='delete'),
        url(r'^meta/$', views.meta, name='meta'),
    ])),
    url(r'^checkouts/', include([
        # READ(Retreive)
        url(r'^$', views.post_products_list, name='list'),
        # CREATE
        # UPDATE
        # DELETE
    ], namespace='checkouts')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 以下適用於網頁讀取"settings.py"中的 MEDIA_URL 與 MEDIA_ROOT 所用
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
