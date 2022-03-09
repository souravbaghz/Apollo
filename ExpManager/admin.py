from django.contrib import admin

from ExpManager.models import ExpManager
# Register your models here.
admin.site.site_header = '土拨鼠自动化扫描系统'  # 设置header
admin.site.site_title = '土拨鼠自动化扫描系统'          # 设置title
@admin.register(ExpManager)
class ExpManagerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'vulnid', 'timestamp', 'change']
    list_filter = ['category']
    search_fields = ['name', 'vulnid']
    ordering = ["id"]
    date_hierarchy = 'timestamp'
