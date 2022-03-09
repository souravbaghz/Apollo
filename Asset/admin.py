from django.contrib import admin

from Asset.models import Asset
# Register your models here.
admin.site.site_header = '土拨鼠自动化扫描系统'  # 设置header
admin.site.site_title = '土拨鼠自动化扫描系统'          # 设置title
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['id', 'ipaddress', 'domain', 'ossystem', 'port', 'state', 'protocol', 'service', 'software', 'version', 'timestamp', 'change']
    list_filter = ['ipaddress', 'domain', 'ossystem', 'port', 'state', 'protocol', 'service', 'software', 'timestamp']
    search_fields = ['ipaddress', 'domain', 'ossystem', 'port', 'state', 'protocol', 'service', 'software', 'version']
    ordering = ["id"]
    date_hierarchy = 'timestamp'
