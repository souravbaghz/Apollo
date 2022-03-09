import threading
from django.db import transaction
from VulnerableScan.views import start_scan
from django.contrib import admin, messages
from VulnerableScan.models import VulnerableScanTasks, ExploitRegister, VulnerableScanResult


# Register your models here.
admin.site.site_header = '阿波罗自动化攻击评估系统'  # 设置header
admin.site.site_title = '阿波罗自动化攻击评估系统'  # 设置title


@admin.register(ExploitRegister)
class ExploitRegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'exploit_name', 'category', 'timestamp', 'change']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ["id"]
    date_hierarchy = 'timestamp'


@admin.register(VulnerableScanTasks)
class VulnerableScanTasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'target', 'exploit', 'change']
    list_filter = ['target', 'exploit']
    search_fields = ['name']
    ordering = ["id"]
    date_hierarchy = 'timestamp'

    @transaction.atomic
    def scan(self, request, queryset):
        work_ids = None
        for item in request.POST.lists():
            if item[0] == "_selected_action":
                work_ids = item[1]
        if isinstance(work_ids, list):
            for work_id in work_ids:
                thread = threading.Thread(target=start_scan, args=(work_id,))
                thread.start()
                messages.add_message(request, messages.SUCCESS, '开始扫描%s' % str(work_id))
        else:
            messages.add_message(request, messages.SUCCESS, '扫描异常')

    scan.short_description = "启动扫描"
    scan.icon = 'fa fa-rocket'
    scan.style = 'color:white;'
    scan.type = 'danger'
    scan.confirm = '您确定要启动扫描吗？'
    actions = [scan, ]


@admin.register(VulnerableScanResult)
class VulnerableScanResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_id', 'task_name', 'ip_address', 'port', 'result_flag', 'timestamp', 'detail']
    list_filter = ['result_flag', 'timestamp']
    search_fields = ['task_name', 'timestamp']
    ordering = ["id"]
    date_hierarchy = 'timestamp'
