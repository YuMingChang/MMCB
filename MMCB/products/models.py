# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify
import datetime


class Product(models.Model):
    name = models.CharField('商品名稱', max_length=20)
    notes = models.TextField('商品描述', blank=True, default='')
    raiser = models.PositiveIntegerField('募集人數', null=True, blank=True)
    date = models.DateField('刊登日期', default=datetime.date.today)
    image = models.ImageField('商品圖片', upload_to='ProductImages',
                              null=True, blank=True)
    is_display = models.BooleanField('展示與否', default=True)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '所有商品'
        ordering = ['-date', 'raiser']

    # def __unicode__(self):    It's doesn't work.
    # solve: http://blog.csdn.net/feifashengwu/article/details/12625719
    # __str__ on Python 3,	__unicode__ on Python 2
    def __str__(self):
        return self.name
    __repr__ = __str__


class Detail(models.Model):
    # Django _set error: “'Product' object has no attribute 'detail_set'”:
    # http://stackoverflow.com/questions/10466522/django-set-error-campaign-object-has-no-attribute-charity-set
    product = models.ForeignKey('Product', verbose_name='商品')
    color = models.CharField('商品樣式', max_length=10)
    size = models.CharField('商品尺寸', max_length=10)
    price = models.PositiveIntegerField('商品價格')

    class Meta:
        verbose_name = '內容'
        verbose_name_plural = '所有內容'

    def __str__(self):
        return self.color + " - " + self.size
    __repr__ = __str__

# Introduce django database Field Type:
# http://blog.csdn.net/pipisorry/article/details/45725953


def get_image_filename(instance, filename):
    title = instance.product.name
    slug = slugify(title, allow_unicode=True)
    return "ProductImages/%s-%s" % (slug, filename)


class Images(models.Model):
    product = models.ForeignKey('Product', verbose_name='商品')
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='商品內容圖片',
                              null=True, blank=True, )

    class Meta:
        verbose_name = '商品圖片'
        verbose_name_plural = '所有商品圖片'
