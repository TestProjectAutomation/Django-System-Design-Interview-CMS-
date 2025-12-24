from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # CMS Content
    path('', include('apps.content.urls')),
]
