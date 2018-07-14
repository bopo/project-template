# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel


# 国家表    
class Country(TimeStampedModel):
    name = models.CharField(verbose_name=_(u'国家名称'), max_length=100, default='')
    flag = models.ImageField(verbose_name=_(u'国家图标'), max_length=100, default='')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = _(u'国家数据')
        verbose_name_plural = _(u'国家数据')


# 省份表
class Province(TimeStampedModel):
    country = models.ForeignKey(Country, verbose_name=_(u'国家'), null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(verbose_name=_(u'标题'), max_length=100, default='')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = _(u'省份数据')
        verbose_name_plural = _(u'省份数据')


# 城市数据
class City(TimeStampedModel):
    country = models.ForeignKey(Country, verbose_name=_(u'国家'), null=True, blank=True, on_delete=models.SET_NULL)
    province = models.ForeignKey(Province, verbose_name=_(u'省份'), null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(verbose_name=_(u'城市'), max_length=10, null=False, default='')
    maps = models.CharField(verbose_name=_(u'坐标'), max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _(u'城市数据')
        verbose_name_plural = _(u'城市数据')
        


# 公交线路表
class Busline(TimeStampedModel):
    version = models.CharField(verbose_name=_(u'版本号'), max_length=10, null=False, default='1.0.0')
    depends = models.CharField(verbose_name=_(u'依赖版本'), max_length=10, null=True, blank=True)
    install = models.URLField(verbose_name=_(u'下载链接'), name='install', null=True)
    sha1sum = models.CharField(verbose_name=_(u'校验码'), max_length=64, null=True, blank=True)
    summary = models.TextField(verbose_name=_(u'日志'), default='')
    constraint = models.BooleanField(verbose_name=_(u'强更'), default=False)

    def __str__(self):
        return self.version

    class Meta:
        verbose_name = _(u'公交线路')
        verbose_name_plural = _(u'公交线路')
        


# 城市铁路表
class Subway(TimeStampedModel):
    score = models.CharField(verbose_name=_(u'版本号'), max_length=1000, null=False, default='1.0.0')
    nickname = models.CharField(verbose_name=_(u'依赖版本'), max_length=100, null=True, blank=True)
    install = models.URLField(verbose_name=_(u'下载链接'), name='install', null=True)
    sha1sum = models.CharField(verbose_name=_(u'校验码'), max_length=64, null=True, blank=True)
    summary = models.TextField(verbose_name=_(u'日志'), default='')
    constraint = models.BooleanField(verbose_name=_(u'强更'), default=False)

    def __str__(self):
        return self.version

    class Meta:
        verbose_name = _(u'城市铁路')
        verbose_name_plural = _(u'城市铁路')
