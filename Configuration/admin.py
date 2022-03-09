import threading
from django.db import transaction
from Configuration.views import service_start
from django.contrib import admin, messages
from Configuration.models import Configuration, Services
# Register your models here.
admin.site.site_header = '阿波罗自动化攻击评估系统'  # 设置header
admin.site.site_title = '阿波罗自动化攻击评估系统'          # 设置title


@admin.register(Configuration)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'value', 'count', 'port', 'ipaddress', 'domain', 'change']
    list_filter = ['name',]
    search_fields = ['name', 'user']
    ordering = ["id"]


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ipaddress', 'port', 'domain', 'change']
    search_fields = ['name']
    ordering = ["id"]

    @transaction.atomic
    def start(self, request, queryset):
        work_ids = None
        for item in request.POST.lists():
            if item[0] == "_selected_action":
                work_ids = item[1]
        if isinstance(work_ids, list):
            for work_id in work_ids:
                thread = threading.Thread(target=service_start, args=(work_id,))
                thread.start()
                messages.add_message(request, messages.SUCCESS, '启动服务%s' % str(work_id))
        else:
            messages.add_message(request, messages.SUCCESS, '启动服务异常')

    start.short_description = "启动服务"
    start.icon = 'fa fa-rocket'
    start.style = 'color:white;'
    start.type = 'danger'
    start.confirm = '您确定要启动服务吗？'
    actions = [start, ]