# Generated by Django 4.0.1 on 2022-03-08 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expmanager',
            options={'verbose_name': '负载管理', 'verbose_name_plural': '负载管理'},
        ),
        migrations.RemoveField(
            model_name='expmanager',
            name='command',
        ),
        migrations.RemoveField(
            model_name='expmanager',
            name='expflag',
        ),
        migrations.AlterField(
            model_name='expmanager',
            name='category',
            field=models.CharField(choices=[('1', 'WEB漏洞'), ('2', '系统漏洞')], max_length=2, verbose_name='漏洞类型'),
        ),
        migrations.AlterField(
            model_name='expmanager',
            name='fileobj',
            field=models.FileField(null=True, upload_to='MyCMS/exp/', verbose_name='负载上传'),
        ),
    ]
