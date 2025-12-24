from django.shortcuts import render, get_object_or_404
from .models import Post, Page

def home(request):
    posts = Post.objects.filter(status='published')
    return render_with_theme(request, 'home.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render_with_theme(request, 'post_detail.html', {'post': post})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, status='published')
    return render_with_theme(request, page.template_name, {'page': page})

def render_with_theme(request, template_name, context=None):
    if context is None:
        context = {}
    theme = getattr(request, 'active_theme', 'default')
    return render(request, f"{theme}/{template_name}", context)
