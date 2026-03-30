from django.db import models
from django.contrib.auth import get_user_model

from apps.item.models import Item
User = get_user_model()

class Order(models.Model):
    class Payment(models.IntegerChoices):
        wxpay = 1, '微信'
        alipay = 2, '支付宝'

    class Status(models.IntegerChoices):
        pending = 0, '待处理'
        success = 1, '已支付'
        fail = 2, '未支付'

    trade_id = models.CharField(editable=False, verbose_name='订单ID')
    order_id = models.CharField(max_length=100, null=True, blank=True, verbose_name='支付平台订单号')
    amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='金额')
    payment = models.IntegerField(choices=Payment.choices, verbose_name='支付方式')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='支付时间')
    status = models.IntegerField(choices=Status.choices, default=Status.pending, verbose_name='订单状态')

    item = models.ForeignKey(Item, related_name='orders', on_delete=models.SET_NULL, null=True, verbose_name='下单项目')
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, verbose_name='下单用户')
    class Meta:
        db_table = 'order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name