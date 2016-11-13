from django.db import models
from django.core import validators
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
import allauth.app_settings


class PersonalInfo(models.Model):
    GENDER = (
        ('M', '男性'),
        ('F', '女性'),
    )
    user = models.OneToOneField(allauth.app_settings.USER_MODEL)
    name = models.CharField(_('姓名'), max_length=16)
    gender = models.CharField(_('性別'), max_length=1, choices=GENDER, default=GENDER[1][0])
    birthday = models.DateField(_('生日'), help_text=_('範例：1993/11/29'))
    phone = models.CharField(
        _('手機'), max_length=10, help_text=_('範例：0912456999'),
        validators=[validators.RegexValidator(
            r'^09\d{8}$', _('請輸入正確的手機號碼'), 'invalid')])
    email = models.EmailField()
    money = models.PositiveIntegerField(_('已消費金額'), default=0)

    class Meta:
        verbose_name = '會員資料'
        verbose_name_plural = '所有會員資料'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Addresses(models.Model):
    personalinfo = models.ForeignKey('PersonalInfo', verbose_name=_('會員'))
    address = models.CharField(
        _('地址'), max_length=64, blank=True, default='',
    )

    class Meta:
        verbose_name = '地址'
        verbose_name_plural = '所有地址'

    def __str__(self):
        return self.address
    __repr__ = __str__


# alphanumeric = RegexValidator(r'^\d{5,6}$', '只能輸入5~6位數字') #Only alphanumeric characters are allowed.
class Accounts(models.Model):
    personalinfo = models.ForeignKey('PersonalInfo', verbose_name=_('會員'))
    account = models.CharField(
        _('匯款帳號(5碼)/無摺局號(6碼)'), max_length=6,
        blank=True, default='', validators=[RegexValidator(r'^\d{5,6}$', '請輸入5位帳號或6位局號！')],
    )

    class Meta:
        verbose_name = '匯款帳號/無摺局號'
        verbose_name_plural = '所有匯款帳號/無摺局號'

    def __str__(self):
        return self.account
    __repr__ = __str__


class FamilyNumber(models.Model):
    personalinfo = models.ForeignKey('PersonalInfo', verbose_name=_('會員'))
    number = models.CharField(
        _('全家店鋪號'), max_length=6,
        blank=True, default='', validators=[RegexValidator(r'^\d{6}$', '請輸入6位全家店鋪號！')],
    )

    class Meta:
        verbose_name = '全家店鋪號'
        verbose_name_plural = '所有全家店鋪號'

    def __str__(self):
        return self.number
    __repr__ = __str__
