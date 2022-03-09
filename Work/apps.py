from django.apps import AppConfig
from django.contrib import admin

#admin.site.site_title = '小白龙'
class WorkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Work'
    verbose_name = "工作"
