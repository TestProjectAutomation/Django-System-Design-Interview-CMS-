from rest_framework.generics import ListAPIView
from .models import Post, Page, Article
from .serializers import PostSerializer

class PostListAPI(ListAPIView):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer

class PageListAPI(ListAPIView):
    queryset = Page.objects.filter(status='published')
    serializer_class = PostSerializer

class ArticleListAPI(ListAPIView):
    queryset = Article.objects.filter(status='published')
    serializer_class = PostSerializer