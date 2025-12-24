from .models import SiteSetting

class ThemeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setting = SiteSetting.objects.first()
        request.active_theme = setting.active_theme if setting else 'default'
        return self.get_response(request)
