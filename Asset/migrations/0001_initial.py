# Generated by Django 4.0.1 on 2022-03-08 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='序号')),
                ('ipaddress', models.GenericIPAddressField(db_column='ipaddress', verbose_name='地址')),
                ('domain', models.TextField(db_column='domain', verbose_name='域名')),
                ('ossystem', models.TextField(db_column='ossystem', null=True, verbose_name='操作系统')),
                ('port', models.IntegerField(db_column='port', verbose_name='端口')),
                ('state', models.CharField(choices=[('0', '关闭'), ('1', '开放'), ('2', '阻断')], max_length=2, verbose_name='端口状态')),
                ('protocol', models.TextField(db_column='protocol', null=True, verbose_name='协议')),
                ('service', models.TextField(db_column='service', null=True, verbose_name='服务')),
                ('software', models.TextField(db_column='software', null=True, verbose_name='组件')),
                ('version', models.TextField(db_column='version', null=True, verbose_name='版本')),
                ('timestamp', models.DateField(db_column='deadline', verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '资产信息',
                'verbose_name_plural': '资产信息',
            },
        ),
    ]
