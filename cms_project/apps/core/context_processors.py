from .models import SiteSetting, Menu

def site_settings(request):
    settings = SiteSetting.objects.first()
    return {
        'site_name': settings.site_name if settings else 'CMS'
    }

def menus(request):
    menu = Menu.objects.first()
    return {
        'main_menu': menu.menuitem_set.all().order_by('order') if menu else []
    }
