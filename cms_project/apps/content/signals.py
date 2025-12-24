from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def post_published(sender, instance, created, **kwargs):
    if instance.status == 'published':
        print('Post Published:', instance.title)

