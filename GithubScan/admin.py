from django.contrib import admin

from GithubScan.models import GithubScanTask, GithubResult
# Register your models here.
admin.site.site_header = '土拨鼠自动化扫描系统'  # 设置header
admin.site.site_title = '土拨鼠自动化扫描系统'          # 设置title
@admin.register(GithubScanTask)
class GithubScanTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'keyword', 'domain', 'timestamp', 'change']
    list_filter = []
    search_fields = ['name', 'keyword', 'domain']
    ordering = ["id"]
    date_hierarchy = 'timestamp'

@admin.register(GithubResult)
class GithubResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'result', 'timestamp', 'change']
    list_filter = []
    search_fields = ['name']
    ordering = ["id"]
    date_hierarchy = 'timestamp'
