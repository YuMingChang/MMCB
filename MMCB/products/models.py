from django.db import models
import datetime

# Django database Field Type introduct: http://blog.csdn.net/pipisorry/article/details/45725953

class Product(models.Model):
    name        = models.CharField('商品名稱', max_length = 20)                                     # 商品名稱
    notes       = models.TextField('商品描述', blank=True, default='')                              # 商品描述
    raiser      = models.PositiveIntegerField('募集人數')                                           # 募集人數
    date        = models.DateField('刊登日期', default=datetime.date.today)                         # 刊登日期
    image       = models.ImageField('商品圖片', upload_to='ProductImages', null=True, blank=True)   # 商品圖片
    is_display  = models.BooleanField('是否展示', default=True)                                     # 是否展示

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '所有商品'

    # def __unicode__(self):	It's doesn't work.	solve: http://blog.csdn.net/feifashengwu/article/details/12625719
    def __str__(self):                  # __str__ on Python 3,	__unicode__ on Python 2
        return self.name


class Detail(models.Model):
    product     = models.ForeignKey('Product', verbose_name = '商品', related_name='details')                              # 商品外鍵
    color       = models.CharField('商品顏色', max_length = 10)                                     # 商品顏色
    size        = models.CharField('商品尺寸', max_length = 10)                                     # 商品尺寸
    price       = models.PositiveIntegerField('商品價格')                                           # 商品價格

    class Meta:
        verbose_name = '內容'
        verbose_name_plural = '所有內容'

    def __str__(self):                  # __str__ on Python 3,	__unicode__ on Python 2
        return "Color:" + self.color + " Size:" + self.size + " Price:" + str(self.price)
