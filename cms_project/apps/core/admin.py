from django.contrib import admin
from .models import SiteSetting, Media

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'active_theme')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
