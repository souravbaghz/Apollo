# Generated by Django 4.0.1 on 2022-03-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpManager', '0002_alter_expmanager_options_remove_expmanager_command_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expmanager',
            name='vulnid',
            field=models.CharField(db_column='vulnid', max_length=32, null=True, verbose_name='漏洞编号'),
        ),
    ]