from django.contrib import admin

from Result.models import Result
from django.db import transaction
# Register your models here.
admin.site.site_header = '土拨鼠自动化扫描系统'  # 设置header
admin.site.site_title = '土拨鼠自动化扫描系统'          # 设置title
@admin.register(Result)
class ExpManagerAdmin(admin.ModelAdmin):
    list_display = ['realid', 'id', 'taskname', 'vulnname', 'resultflag', 'timestamp', 'detail']
    list_filter = ['resultflag', 'timestamp']
    search_fields = ['taskname', 'vulnname', 'timestamp']
    ordering = ["realid"]
    date_hierarchy = 'timestamp'
