from django.contrib import admin, messages
from .utils import Scan
from Work.models import Work
from django.db import transaction

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ipdst', 'port', 'exp', 'change']
    list_filter = ['ipdst', 'port', 'exp']
    search_fields = ['name', 'ipdst', 'port']
    ordering = ["id"]
    date_hierarchy = 'timestamp'
    @transaction.atomic
    def scan(self, request, queryset):
       workid = None
       for item in request.POST.lists():
           if item[0] == "_selected_action":
               workid = item[1]
       if isinstance(workid, list):
           for id in workid:
               thread = Scan(id)
               thread.start()
               messages.add_message(request, messages.SUCCESS, '开始扫描%s' % str(id))
       else:
           messages.add_message(request, messages.SUCCESS, '扫描异常')


    scan.short_description = "启动扫描"
    scan.icon = 'fa fa-rocket'
    scan.style = 'color:white;'
    scan.type = 'danger'
    scan.confirm = '您确定要启动扫描吗？'
    actions = [scan, ]

