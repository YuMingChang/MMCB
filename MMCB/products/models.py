# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
import datetime

# Introduce django database Field Type: http://blog.csdn.net/pipisorry/article/details/45725953

class Product(models.Model):
    name        = models.CharField('商品名稱', max_length = 20)                                     # 商品名稱
    notes       = models.TextField('商品描述', blank=True, default='')                              # 商品描述
    raiser      = models.PositiveIntegerField('募集人數')                                           # 募集人數
    date        = models.DateField('刊登日期', default=datetime.date.today)                         # 刊登日期
    image       = models.ImageField('商品圖片', upload_to='ProductImages', null=True, blank=True)   # 商品圖片
    is_display  = models.BooleanField('展示與否', default=True)                                     # 是否展示

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '所有商品'
        ordering = ['-date', 'raiser']

    # def __unicode__(self):	It's doesn't work.	solve: http://blog.csdn.net/feifashengwu/article/details/12625719
    def __str__(self):                  # __str__ on Python 3,	__unicode__ on Python 2
        return self.name
    __repr__ = __str__

    def get_absolute_url(self):
        return reverse('posts:list')


class Detail(models.Model):
    # Django _set error: “'Product' object has no attribute 'detail_set'”:
    # http://stackoverflow.com/questions/10466522/django-set-error-campaign-object-has-no-attribute-charity-set
    product     = models.ForeignKey('Product', verbose_name = '商品', related_name='details')                              # 商品外鍵
    color       = models.CharField('商品樣式', max_length = 10)                                     # 商品顏色
    size        = models.CharField('商品尺寸', max_length = 10)                                     # 商品尺寸
    price       = models.PositiveIntegerField('商品價格')                                           # 商品價格

    class Meta:
        verbose_name = '內容'
        verbose_name_plural = '所有內容'

    def __str__(self):                  # __str__ on Python 3,	__unicode__ on Python 2
        return self.color + " - " + self.size
    __repr__ = __str__
