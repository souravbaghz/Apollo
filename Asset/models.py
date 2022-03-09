from django.db import models

# Create your models here.
from django.db import models
from django.utils.html import format_html

from tinymce.models import HTMLField
# Create your models here.


class Asset(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", verbose_name='序号')
    ipaddress = models.GenericIPAddressField(db_column="ipaddress", verbose_name='地址')
    domain = models.TextField(db_column="domain", verbose_name='域名')
    ossystem = models.TextField(db_column="ossystem", verbose_name='操作系统', null=True)
    port = models.IntegerField(db_column="port", verbose_name='端口')
    state_choices = (("0", "关闭"), ("1", "开放"), ("2", "阻断"))
    state = models.CharField(max_length=2, choices=state_choices, verbose_name='端口状态')
    protocol = models.TextField(db_column="protocol", verbose_name='协议', null=True)
    service = models.TextField(db_column="service", verbose_name='服务', null=True)
    software = models.TextField(db_column="software", verbose_name='组件', null=True)
    version = models.TextField(db_column="version", verbose_name='版本', null=True)
    timestamp = models.DateField(db_column="deadline", verbose_name='创建日期')

    def __str__(self):
        return self.ipaddress

    def change(self):
        btn_str = '<a class="btn btn-xs btn-danger" href="{}">' \
                    '<input name="编辑"' \
                    'type="button" id="passButton" ' \
                    'title="passButton" value="编辑">' \
                    '</a>'
        return format_html(btn_str, '%s/change'%self.id)
    change.short_description = '资产编辑'
    class Meta:
        verbose_name = '资产信息'
        verbose_name_plural = verbose_name