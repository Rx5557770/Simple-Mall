from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='内容')

    class Meta:
        verbose_name = '卡片'
        verbose_name_plural = verbose_name


class Home(models.Model):
    web_title = models.CharField(max_length=20, verbose_name='网站标题')
    content = models.TextField(verbose_name='首页内容')

    class Meta:
        verbose_name = '内容'
        verbose_name_plural = verbose_name