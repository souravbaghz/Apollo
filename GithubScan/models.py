from django.db import models

# Create your models here.
from django.db import models
from django.utils.html import format_html


# Create your models here.


class GithubScanTask(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", verbose_name='序号')
    name = models.CharField(max_length=32, db_column="name", verbose_name='任务名称')
    keyword = models.CharField(db_column="keyword", max_length=256, verbose_name='关键字')
    domain = models.CharField(db_column="domain", max_length=256, verbose_name='域名', null=True, blank=True)
    timestamp = models.DateField(db_column="timestamp", verbose_name='创建日期')

    def __str__(self):
        return self.name

    def change(self):
        btn_str = '<a class="btn btn-xs btn-danger" href="{}">' \
                    '<input name="编辑任务"' \
                    'type="button" id="passButton" ' \
                    'title="passButton" value="编辑">' \
                    '</a>'
        return format_html(btn_str, '%s/change'%self.id)
    change.short_description = '任务编辑'

    class Meta:
        verbose_name = '任务管理'
        verbose_name_plural = verbose_name


class GithubScanResult(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", verbose_name='序号')
    name = models.CharField(max_length=32, db_column="name", verbose_name='任务名称')
    keyword = models.CharField(db_column="keyword", max_length=256, verbose_name='关键字',default="")
    domain = models.CharField(db_column="domain", max_length=256, verbose_name='域名', null=True, blank=True)
    url = models.CharField(db_column="url", max_length=256, verbose_name='链接', null=True, blank=True)
    timestamp = models.DateField(db_column="timestamp", verbose_name='创建日期')

    def __str__(self):
        return self.name

    def change(self):
        btn_str = '<a class="btn btn-xs btn-danger" href="{}">' \
                  '<input name="结果查看"' \
                  'type="button" id="passButton" ' \
                  'title="passButton" value="查看">' \
                  '</a>'
        return format_html(btn_str, '%s/change' % self.id)

    change.short_description = '结果查看'

    class Meta:
        verbose_name = '任务管理'
        verbose_name_plural = verbose_name