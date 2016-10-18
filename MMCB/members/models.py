from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
import allauth.app_settings


class PersonalInfo(models.Model):
    SEXUAL = (
        ('M', '男性'),
        ('F', '女性'),
    )
    user = models.OneToOneField(allauth.app_settings.USER_MODEL)
    name = models.CharField(_('姓名（收件人）'), max_length=20)
    sexual = models.CharField(_('性別'), max_length=1, choices=SEXUAL)
    birthday = models.DateField(_('生日'), help_text=_('範例：1993/11/29'))
    phone = models.CharField(
        _('手機'), max_length=10, help_text=_('範例：0912456999'),
        validators=[validators.RegexValidator(
                            r'^09\d{8}$', _('請輸入正確的手機號碼'), 'invalid')])
    email = models.EmailField()
    address = models.CharField('住址', max_length=150)
    # called 'card_number' when this reconstructure.
    accounts = models.CharField(
        _('匯款帳號後五碼'), max_length=5, help_text=_('範例：12345'),
        validators=[validators.RegexValidator(
                            r'^\d{5}$', _('請輸入匯款帳號後五碼'), 'invalid')])
    money = models.PositiveIntegerField(_('儲值金'), default=0)

    class Meta:
        verbose_name = '個資'
        verbose_name_plural = '會員資料'
        ordering = ['id']

    def __str__(self):
        return self.name
    __repr__ = __str__
# ID、姓名、性別、生日、手機、信箱、帳戶後五碼、儲值金
# 郵遞區號、國家、縣市、地址、預設地址
# 預設配送方式、預設付款方式
# 配送店號
