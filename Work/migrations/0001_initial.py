# Generated by Django 4.0.1 on 2022-01-19 08:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ExpManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(db_column='name', max_length=32, verbose_name='任务名称')),
                ('ipdst', models.GenericIPAddressField(db_column='ipdst', default='0.0.0.0', verbose_name='目标地址')),
                ('port', models.IntegerField(db_column='port', default=0, verbose_name='目标端口')),
                ('timestamp', models.DateField(db_column='deadline', default=django.utils.timezone.now, verbose_name='创建日期')),
                ('exp', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ExpManager.expmanager', verbose_name='选择的漏洞')),
            ],
            options={
                'verbose_name': '任务项',
                'verbose_name_plural': '任务项',
            },
        ),
    ]