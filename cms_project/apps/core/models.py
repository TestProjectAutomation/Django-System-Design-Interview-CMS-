from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100)
    active_theme = models.CharField(max_length=50, default='default')

    def __str__(self):
        return self.site_name
