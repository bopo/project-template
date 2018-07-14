# Generated by Django 2.0.6 on 2018-07-03 10:34

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Busline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('version', models.CharField(default='1.0.0', max_length=10, verbose_name='版本号')),
                ('depends', models.CharField(blank=True, max_length=10, null=True, verbose_name='依赖版本')),
                ('install', models.URLField(null=True, verbose_name='下载链接')),
                ('sha1sum', models.CharField(blank=True, max_length=64, null=True, verbose_name='校验码')),
                ('summary', models.TextField(default='', verbose_name='日志')),
                ('constraint', models.BooleanField(default=False, verbose_name='强更')),
            ],
            options={
                'verbose_name': '公交线路',
                'verbose_name_plural': '公交线路',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(default='', max_length=10, verbose_name='城市')),
                ('maps', models.CharField(blank=True, max_length=10, null=True, verbose_name='坐标')),
            ],
            options={
                'verbose_name': '城市数据',
                'verbose_name_plural': '城市数据',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(default='', max_length=100, verbose_name='国家名称')),
                ('flag', models.ImageField(default='', upload_to='', verbose_name='国家图标')),
            ],
            options={
                'verbose_name': '国家数据',
                'verbose_name_plural': '国家数据',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(default='', max_length=100, verbose_name='标题')),
                ('phone', models.CharField(default='', max_length=100, verbose_name='联系电话')),
                ('content', models.TextField(default='', max_length=255, verbose_name='内容详情')),
                ('storage', models.FileField(default='', max_length=255, upload_to='', verbose_name='内容详情')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='发布人')),
            ],
            options={
                'verbose_name': '意见反馈',
                'verbose_name_plural': '意见反馈',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(default='', max_length=100, verbose_name='标题')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Country', verbose_name='国家')),
            ],
            options={
                'verbose_name': '省份数据',
                'verbose_name_plural': '省份数据',
            },
        ),
        migrations.CreateModel(
            name='Subway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('score', models.CharField(default='1.0.0', max_length=1000, verbose_name='版本号')),
                ('nickname', models.CharField(blank=True, max_length=100, null=True, verbose_name='依赖版本')),
                ('install', models.URLField(null=True, verbose_name='下载链接')),
                ('sha1sum', models.CharField(blank=True, max_length=64, null=True, verbose_name='校验码')),
                ('summary', models.TextField(default='', verbose_name='日志')),
                ('constraint', models.BooleanField(default=False, verbose_name='强更')),
            ],
            options={
                'verbose_name': '城市铁路',
                'verbose_name_plural': '城市铁路',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('version', models.CharField(default='1.0.0', max_length=10, verbose_name='版本号')),
                ('depends', models.CharField(blank=True, max_length=10, null=True, verbose_name='依赖版本')),
                ('install', models.URLField(null=True, verbose_name='下载链接')),
                ('sha1sum', models.CharField(blank=True, max_length=64, null=True, verbose_name='校验码')),
                ('channel', models.CharField(choices=[('1000', '官网'), ('1001', '91助手'), ('1002', '百度'), ('1003', '安卓'), ('1004', '豌豆荚'), ('1005', '应用宝'), ('1006', '360'), ('1007', '应用汇'), ('1008', '魅族'), ('1009', 'N多网'), ('1010', 'PP助手'), ('1011', '淘宝'), ('1012', '机锋网'), ('1013', '金立'), ('1014', '小米'), ('1015', '华为'), ('1016', '搜狗'), ('1017', '安智'), ('1018', '沃商店'), ('1019', 'itools'), ('1020', '电信爱游戏'), ('1021', '优亿市场'), ('1022', '应用贝'), ('1023', 'googleplay'), ('1024', '安粉网')], max_length=10, verbose_name='渠道')),
                ('summary', models.TextField(default='', verbose_name='日志')),
                ('platform', models.CharField(choices=[('ios', 'IOS'), ('android', 'Android')], default='android', max_length=50, verbose_name='APP平台')),
                ('constraint', models.BooleanField(default=False, verbose_name='强更')),
            ],
            options={
                'verbose_name': 'APP 版本升级',
                'verbose_name_plural': 'APP 版本升级',
            },
        ),
        migrations.AlterUniqueTogether(
            name='version',
            unique_together={('version', 'channel')},
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Country', verbose_name='国家'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Province', verbose_name='省份'),
        ),
    ]