from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from members.models import PersonalInfo
from products.models import Detail


# Create your models here.

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
        'UnPaid': 'UP',
        'Paid': 'PA',
        'PaidComfirm': 'PC',
        'WaitToSend': 'WS',
        'Sent': 'SN',
        'Abandon': 'AB',
        'CancelAbandon': 'CA',
        'AbandonComfirm': 'AC',
        'Abandoned': 'AD',
    }
    ORDER_STATUS = (
        (STATUS['UnPaid'], '待付款/匯款'),
        (STATUS['Paid'], '通知已付款'),
        (STATUS['PaidComfirm'], '確認已付款'),
        (STATUS['WaitToSend'], '商品準備中'),
        (STATUS['Sent'], '商品已寄出'),
        (STATUS['Abandon'], '放棄此訂單'),
        (STATUS['CancelAbandon'], '取消放棄此訂單'),
        (STATUS['AbandonComfirm'], '待賣家確認放棄'),
        (STATUS['Abandoned'], '已放棄'),
    )

    number = models.DecimalField('訂單編號', max_digits=16, decimal_places=0,
                                 validators=[MinValueValidator(0)])
    shopper = models.ForeignKey(PersonalInfo, verbose_name='買家')
    order_date = models.DateTimeField('訂購時間', default=timezone.now)
    sold_goods = models.ManyToManyField(Detail, verbose_name='已買商品')
    freight = models.PositiveIntegerField('運費')
    total = models.PositiveIntegerField('總額')
    notes = models.TextField('備註', max_length=200, default='')
    status = models.CharField(max_length=2, choices=ORDER_STATUS, default=STATUS['UnPaid'])
    order_notes = models.TextField('訂單清單', default='')

    class Meta:
        verbose_name = '購物清單'
        verbose_name_plural = '所有購物清單'
        ordering = ['-order_date']

    def get_sold_goods(self):
        return "\n".join([str(good) for good in self.sold_goods.all()])
