# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel
from djmoney.models.fields import MoneyField

PLATFORM_CHOICES = Choices(
    ('ios', _('IOS')),
    ('android', _('Android')),
)

CHANNEL_CHOICES = (
    ('1000', "官网"),
    ('1001', "91助手"),
    ('1002', "百度"),
    ('1003', "安卓"),
    ('1004', "豌豆荚"),
    ('1005', "应用宝"),
    ('1006', "360"),
    ('1007', "应用汇"),
    ('1008', "魅族"),
    ('1009', "N多网"),
    ('1010', "PP助手"),
    ('1011', "淘宝"),
    ('1012', "机锋网"),
    ('1013', "金立"),
    ('1014', "小米"),
    ('1015', "华为"),
    ('1016', "搜狗"),
    ('1017', "安智"),
    ('1018', "沃商店"),
    ('1019', "itools"),
    ('1020', "电信爱游戏"),
    ('1021', "优亿市场"),
    ('1022', "应用贝"),
    ('1023', "googleplay"),
    ('1024', "安粉网")
)


class Version(TimeStampedModel):
    version = models.CharField(verbose_name=_(u'版本号'), max_length=10, null=False, default='1.0.0')
    depends = models.CharField(verbose_name=_(u'依赖版本'), max_length=10, null=True, blank=True)
    install = models.URLField(verbose_name=_(u'下载链接'), name='install', null=True)
    sha1sum = models.CharField(verbose_name=_(u'校验码'), max_length=64, null=True, blank=True)
    channel = models.CharField(verbose_name=_(u'渠道'), max_length=10, blank=False, choices=CHANNEL_CHOICES)
    summary = models.TextField(verbose_name=_(u'日志'), default='')
    platform = models.CharField(verbose_name=_(u'APP平台'), max_length=50, default='android', choices=PLATFORM_CHOICES)
    constraint = models.BooleanField(verbose_name=_(u'强更'), default=False)

    def __str__(self):
        return self.version

    # def save(self, *args, **kwargs):
    #     import hashlib
    #     sha1 = hashlib.sha1()

    #     for chunk in self.install.chunks():
    #         sha1.update(chunk)

    #     self.sha1sum = sha1.hexdigest()
    #     self.install.name = '%s.apk' % self.sha1sum
    #     super(Version, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'版本管理')
        verbose_name_plural = _(u'版本管理')
        unique_together = ('version', 'channel',)
        ordering = ('-created',)

        # def on_delete(sender, instance, **kwargs):
        #     instance.install.delete(save=False)

        # models.signals.post_delete.connect(on_delete, sender=Version)


# 意见反馈表
class Feedback(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'发布人'), null=True, blank=True,
                              on_delete=models.SET_NULL)
    title = models.CharField(verbose_name=_(u'标题'), max_length=100, default='')
    phone = models.CharField(verbose_name=_(u'联系电话'), max_length=100, default='')
    content = models.TextField(verbose_name=_(u'内容详情'), max_length=255, default='')
    storage = models.FileField(verbose_name=_(u'内容详情'), max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['-id']
        verbose_name = _(u'意见反馈')
        verbose_name_plural = _(u'意见反馈')


class BankAccount(models.Model):
    balance = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
