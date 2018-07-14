import binascii
import os

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from jsonfield import JSONField
from model_utils.models import TimeStampedModel
from pilkit.processors import ResizeToFill


class Profile(models.Model):
    '''
    该接口更新接受PUT方法
    性别字段英文对应汉字为:
    male:男
    female:女
    提交的数据要用英文.获取时候api也是英文, 要客户端自己做下转换.
    '''
    GENDER_CHOICES = (('', '未知'), ('male', '男'), ('female', '女'))
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 unique=True, db_index=True, related_name='profile',
                                 on_delete=models.CASCADE)

    name = models.CharField(verbose_name=_(u'姓名'), blank=True, max_length=100, db_index=True)
    nick = models.CharField(verbose_name=_(u'昵称'), blank=True, null=True, max_length=100, db_index=True, default='')

    mobile = models.CharField(verbose_name=_(u'电话号码'), max_length=50, default='')
    gender = models.CharField(verbose_name=_(u'性别'), max_length=10, choices=GENDER_CHOICES, default=u'male')
    credit = models.IntegerField(_(u'用户积分'), default='50')
    avatar = ProcessedImageField(verbose_name=_(u'头像'),
                                 upload_to='avatar', processors=[ResizeToFill(320, 320)],
                                 format='JPEG', null=True, default='avatar/default.jpg'
                                 )

    birthday = models.DateField(_(u'生日'), blank=True, null=True)
    balance = models.DecimalField(verbose_name=_(u'数字币余额'), max_digits=10, decimal_places=2, default=0.00)
    expired = models.DateTimeField(verbose_name=_(u'到期时间'), blank=True, null=True)

    # @property
    # def qrcode(self, request):
    #     reverse('q', args=[short_url.encode_url(self.pk)], request=request)

    def __str__(self):
        return self.name

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    class Meta:
        verbose_name = _(u'用户信息')
        verbose_name_plural = _(u'用户信息')


class Notification(TimeStampedModel):
    '''
    用户消息
    '''
    subject = models.CharField(verbose_name=_(u'主题'), max_length=255, default='')
    content = models.TextField(verbose_name=_(u'正文'), default='')

    extra = JSONField(verbose_name=u'附加内容', default={'data': "", 'type': ""})
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'推送给用户'),
                              null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '<{} : {}>'.format(self.owner, self.subject)

    class Meta:
        ordering = ('-pk',)
        verbose_name = _(u'消息中心')
        verbose_name_plural = _(u'消息中心')
