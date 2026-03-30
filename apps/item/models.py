from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='分类名')
    is_show = models.BooleanField(default=True, verbose_name='显示')

    class Meta:
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='项目名')
    desc = models.TextField(null=True, blank=True, verbose_name='介绍')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    return_url = models.URLField(verbose_name='文件地址')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', related_name='items')
    is_show = models.BooleanField(default=True, verbose_name='显示')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'item'
        verbose_name = '项目'
        verbose_name_plural = verbose_name


class Purchase(models.Model):
    """购买记录表：关联用户与商品"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase', verbose_name='用户')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchase', verbose_name='项目')
    purchased_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        # 关键约束：同一用户 + 同一商品 只能有一条记录
        constraints = [
            models.UniqueConstraint(fields=['user', 'item'], name='unique_user_item')
        ]
        db_table = 'purchase'
        verbose_name = '购买记录'
        verbose_name_plural = verbose_name