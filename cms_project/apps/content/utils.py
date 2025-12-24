from django.shortcuts import render

def themed_render(request, template_name, context):
    theme = getattr(request, 'active_theme', 'default')
    return render(request, f"{theme}/templates/{template_name}", context)
