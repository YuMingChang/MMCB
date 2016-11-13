from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from posts import views

urlpatterns = [
    url(r'^$', views.post_page, name='page'),
    url(r'^products/', include([
        # READ(Retreive)
        url(r'^$', views.post_products_list, name='productlist'),
        # CREATE(Prodcut)
        url(r'^create/$', views.post_product_add, name='create'),

        # CREATE(Item)
        url(r'^add_item/$', views.post_item_add, name='add_item'),
        url(r'^add_item/(?P<good_id>\d+)/$', views.post_item_add, name='add_item'),

        # UPDATE
        url(r'^edit/(?P<good_id>\d+)/$', views.post_product_update, name='update'),

        # DELETE
        url(r'^delete/(?P<good_id>\d+)/$', views.post_product_delete, name='delete'),
        url(r'^meta/$', views.meta, name='meta'),
    ])),
    url(r'^checkouts/', include([
        # READ(Retreive)
        url(r'^$', views.post_products_list, name='list'),
        # CREATE
        # UPDATE
        # DELETE
    ], namespace='checkouts')),
    url(r'^orders/', include([
        # READ(Retreive)
        url(r'^$', views.post_orders_list, name='orderlist'),
        url(r'^(?P<number>\d+)/$', views.posts_order, name='order'),
        # CREATE(Prodcut)
        # UPDATE
        url(r'^(?P<number>\d+)/(?P<do>.+)/(?P<fmnumber>\d+)/(?P<shiptime>.+)/$', views.posts_order_update, name='order_update'),
        # DELETE
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 以下適用於網頁讀取"settings.py"中的 MEDIA_URL 與 MEDIA_ROOT 所用
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
