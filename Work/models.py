import django.utils.timezone as timezone
from django.db import models
from django.utils.html import format_html

from ExpManager.models import ExpManager
# Create your models here.


class Work(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", verbose_name='编号')
    name = models.CharField(max_length=32, db_column="name", verbose_name='任务名称')
    ipdst = models.GenericIPAddressField(db_column="ipdst", verbose_name='目标地址', default="0.0.0.0")
    port = models.IntegerField(db_column="port", verbose_name='目标端口', default=0)
    exp = models.ForeignKey(ExpManager, verbose_name="选择的漏洞", on_delete=models.CASCADE, default=None)
    timestamp = models.DateField(db_column="deadline", verbose_name='创建日期',default=timezone.now)  # 截止日期
    def change(self):
        btn_str = '<a class="btn btn-xs btn-danger" href="{}">' \
                    '<input name="编辑任务"' \
                    'type="button" id="passButton" ' \
                    'title="passButton" value="修改">' \
                    '</a>'
        return format_html(btn_str, '%s/change'%self.id)
    change.short_description = '任务编辑'
    class Meta:
        verbose_name = '任务项'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


