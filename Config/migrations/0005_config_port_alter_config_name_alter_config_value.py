# Generated by Django 4.0.1 on 2022-03-08 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Config', '0004_config_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='port',
            field=models.TextField(blank=True, db_column='port', null=True, verbose_name='端口列表'),
        ),
        migrations.AlterField(
            model_name='config',
            name='name',
            field=models.CharField(choices=[('1', 'Virustotal接口'), ('2', '钉钉接口'), ('3', 'Github接口'), ('4', '钟馗之眼接口'), ('5', '佛法接口'), ('6', '系统线程数'), ('7', '系统IP地址'), ('8', '系统域名配置'), ('9', '企业常用端口'), ('10', '关键端口')], max_length=2, unique=True, verbose_name='配置名称'),
        ),
        migrations.AlterField(
            model_name='config',
            name='value',
            field=models.TextField(blank=True, db_column='value', null=True, verbose_name='Token令牌'),
        ),
    ]