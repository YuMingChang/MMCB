from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from members.models import PersonalInfo
from products.models import Item
# 訂單編號、買家、連絡賣家、查看訂單
# 結帳時間
# 商品名稱/商品編號 (多個)
# 數量/商品總價
# 運費
# 結帳總金額
# 交易狀況（待付款，請轉帳至.../賣家確認金額中/已付款）
# 可執行動作 （通知已付款、(放棄此訂單/待賣家確認放棄/已放棄)）

# 訂單資訊:
# 賣出時間、商品名稱/編號、數量/商品總價、運費、總金額、付款方式/交易狀況、可執行動作（通知出貨）
# 會員帳號(ID)、姓名、手機、信箱、剩餘儲值金

# 買家交易明細:
# 付款資訊: 匯款銀行名、匯款銀行代碼、轉出帳號末五碼、匯款人姓名、匯款時間
# 收件人資料：收件人姓名、手機、收件地址

# 給賣家的話:

# 賣家出貨資訊:
# 出貨資料：出貨進度、預計出貨方式、預計出貨時間
# 給買家的話


class PurchaseOrder(models.Model):
    STATUS = {
        'Unpaid': 'UPD',
        'Paid': 'PAD',
        'ComfirmPayment': 'CFP',
        'Shipping': 'SPN',
        'Shipped': 'SPD',
        'Abandon': 'ABN',
        'CancelAbandonment': 'CCA',
        'ComfirmAbandonment': 'CFA',
        'Abandoned': 'ABD',
    }
    ORDER_STATUS = (
        (STATUS['Unpaid'], '待付款/匯款'),
        (STATUS['Paid'], '通知已付款'),
        (STATUS['ComfirmPayment'], '確認已付款'),
        (STATUS['Shipping'], '商品準備中'),
        (STATUS['Shipped'], '商品已寄出'),
        (STATUS['Abandon'], '放棄此訂單'),
        (STATUS['CancelAbandonment'], '取消放棄此訂單'),
        (STATUS['ComfirmAbandonment'], '待賣家確認放棄'),
        (STATUS['Abandoned'], '已放棄'),
    )
    METHOD = {
        'Family': 'FML',
        'KerryTJ': 'KTJ',
    }
    SHIP_METHOD = (
        (METHOD['Family'], '全家'),
        (METHOD['KerryTJ'], '大榮貨運'),
    )

    number = models.DecimalField(_('訂單編號'), max_digits=16, decimal_places=0,
                                 validators=[MinValueValidator(0)])
    buyer = models.ForeignKey(PersonalInfo, verbose_name=_('買家'))
    order_time = models.DateTimeField(_('訂購時間'), default=timezone.now)
    sold_goods = models.ManyToManyField(Item, verbose_name=_('已買商品'))
    freight = models.PositiveSmallIntegerField(_('運費'))
    ship_method = models.CharField(_('運送方式'), max_length=3, choices=SHIP_METHOD, default=METHOD['KerryTJ'])
    address = models.CharField(_('寄送地址'), max_length=64, default='')
    total = models.PositiveIntegerField(_('總額'))
    buyer_notes = models.TextField(_('備註'), default='')
    status = models.CharField(_('訂單狀態'), max_length=3, choices=ORDER_STATUS, default=STATUS['Unpaid'])
    order_notes = models.TextField(_('訂單清單'), default='')
    remittance_account = models.CharField(_('匯款帳號'), max_length=6, default="")
    remittance_time = models.DateTimeField(_('匯款日期時間'), blank=True, null=True)
    shipment_number = models.CharField(_('包裹貨件編號'), max_length=13, default="")
    shipment_time = models.DateTimeField(_('寄出日期時間'), blank=True, null=True)
    renounce_time = models.DateTimeField(_('放棄日期時間'), blank=True, null=True)

    class Meta:
        verbose_name = '購物清單'
        verbose_name_plural = '所有購物清單'
        ordering = ['-order_time']

    def get_sold_goods(self):
        return "\n".join([str(good) for good in self.sold_goods.all()])
