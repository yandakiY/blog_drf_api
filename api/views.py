from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from blog.models import Category , Article , Comments , UserBlog
from .serializers import CategorySerializer , CategoryCreateSerializer , ArticleSerializer , ArticleCreateSerializer , CommentsSerializer , CommentsCreateSerializer

# Create your views here.

class CategoryViewSet(ModelViewSet):
    
    queryset = Category.objects.all()
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return CategorySerializer
        
        return CategoryCreateSerializer
    
    
class ArticleViewSet(ModelViewSet):
    
    queryset = Article.objects.all()
    
    def get_serializer_context(self):
        
        user_id = self.request.user.id
        return {'user_id':user_id}
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return ArticleSerializer
        
        return ArticleCreateSerializer
    

class CommentsViewSet(ModelViewSet):
    
    # Add private props (Article private)
    # like a article, dislike a article
    
    def get_queryset(self):
        # user_id = self.request.user.id
        return Comments.objects.all()
    
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return CommentsSerializer
        
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return CommentsCreateSerializer
        
        return CommentsSerializer
    
    
    def get_serializer_context(self):
        # id of user authenticated
        user_id = self.request.user.id
        # id article
        return {
            'user_id': user_id,
            'article_id': self.kwargs['article_pk']
        }
        
