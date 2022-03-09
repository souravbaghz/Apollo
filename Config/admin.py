from django.contrib import admin

from Config.models import Config
# Register your models here.
admin.site.site_header = '土拨鼠自动化扫描系统'  # 设置header
admin.site.site_title = '土拨鼠自动化扫描系统'          # 设置title
@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'value', 'count', 'port', 'ipaddress', 'domain', 'timestamp', 'change']
    list_filter = ['name', 'timestamp']
    search_fields = ['name', 'user']
    ordering = ["id"]
    date_hierarchy = 'timestamp'
