# Generated by Django 4.0.1 on 2022-03-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Config', '0003_alter_config_domain_alter_config_ipaddress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='count',
            field=models.IntegerField(blank=True, db_column='count', default=10, null=True, verbose_name='配置值'),
        ),
    ]
