from django.contrib import admin
from .models import Post, Page

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')

def has_change_permission(self, request, obj=None):
    if request.user.groups.filter(name='Editor').exists():
        return True
    return super().has_change_permission(request, obj)
