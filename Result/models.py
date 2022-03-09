from django.db import models

# Create your models here.
from django.db import models
from django.utils.html import format_html


# Create your models here.
class Result(models.Model):
    realid = models.AutoField(primary_key=True, db_column="rid", verbose_name='序号')
    id = models.IntegerField(db_column="id", verbose_name='对应工单序号')
    taskname = models.CharField(max_length=32, db_column="name", verbose_name='工单名称')
    vulnname = models.CharField(max_length=32, db_column="vulnid", verbose_name='漏洞编号')
    ipaddress = models.GenericIPAddressField(db_column="ipdst", verbose_name='目标地址', null=True)
    port = models.IntegerField(db_column="port", verbose_name='目标端口', null=True)
    description = models.TextField(db_column="description", verbose_name='任务过程描述')
    resultflag = models.BooleanField(db_column="result", verbose_name='测试结果')
    timestamp = models.DateField(db_column="timestamp", verbose_name='结束日期')

    def __str__(self):
        return "%s号工单" % str(id)

    def detail(self):
        btn_str = '<a class="btn btn-xs btn-danger" href="{}">' \
                  '<input name="查看详情"' \
                  'type="button" id="passButton" ' \
                  'title="passButton" value="查看">' \
                  '</a>'
        return format_html(btn_str, '%s/change' % str(self.realid))

    detail.short_description = '工单详情'

    class Meta:
        verbose_name = '工单结果'
        verbose_name_plural = verbose_name
