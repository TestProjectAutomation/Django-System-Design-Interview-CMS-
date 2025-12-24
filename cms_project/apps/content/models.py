from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.fields import GenericRelation
from apps.seo.models import SEO


class Content(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(Content):
    category = models.CharField(max_length=100)
    seo = GenericRelation(SEO)

    def __str__(self):
        return self.title

class Page(Content):
    template_name = models.CharField(max_length=100, default='page.html')

    def __str__(self):
        return self.title


