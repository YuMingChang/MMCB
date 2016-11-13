from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    name = models.CharField(_('商品名稱'), max_length=16)
    notes = models.TextField(_('商品描述'), blank=True, default='')
    onshelf_time = models.DateTimeField(_('上架時間'), default=timezone.now)
    image = models.ImageField(_('商品陳列圖片'), upload_to='ProductImages', null=True, blank=True)
    is_display = models.BooleanField(_('是否陳列商品'), default=True)
    freight_only = models.BooleanField(_('限制只能貨運'), default=False)

    def thumbnail(self):
        return mark_safe('<img src="/media/%s" width="30" height="30" />' % (self.image))
    thumbnail.short_description = 'Thumbnail'

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '所有商品'
        ordering = ['-onshelf_time', '-id']

    def __str__(self):
        return self.name
    __repr__ = __str__


class Images(models.Model):
    def get_image_filename(instance, filename):
        title = instance.product.name
        slug = slugify(title, allow_unicode=True)
        return "ProductImages/%s - %s" % (slug, filename)

    product = models.ForeignKey('Product', verbose_name=_('商品'))
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name=_('商品內容圖片'),
                              blank=True, null=True, )

    class Meta:
        verbose_name = '商品內容圖片'
        verbose_name_plural = '所有商品內容圖片'


class Item(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('商品'))
    style = models.CharField(_('商品款式'), max_length=8)
    size = models.CharField(_('商品尺寸'), max_length=8)
    price = models.PositiveSmallIntegerField(_('商品價格'), default=0)
    pre_order = models.SmallIntegerField(_('預購量'), default=0)
    selling = models.PositiveSmallIntegerField(_('已出貨量'), default=0)
    selling_volume = models.PositiveSmallIntegerField(_('總出貨量'), default=0)
    reset_time = models.DateTimeField(_('上次歸零時間'), blank=True, null=True)
    is_reset = models.BooleanField(_('是否歸零'), default=False)
    is_shortage = models.BooleanField(_('是否缺貨'), default=False)

    class Meta:
        verbose_name = '商品項目'
        verbose_name_plural = '所有商品項目'

    def __str__(self):
        return "{} - {}".format(self.style, self.size)
    __repr__ = __str__
