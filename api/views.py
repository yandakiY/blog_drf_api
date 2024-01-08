from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from blog.models import Category , Article , Comments , UserBlog , LikeArticle , DislikeArticle
from .serializers import CategorySerializer , CategoryCreateSerializer , ArticleSerializer , ArticleCreateSerializer , CommentsSerializer , CommentsCreateSerializer , LikeArticleSerializer ,LikeAnArticleSerializer, DisLikeArticleSerializer , DisLikeAnArticleSerializer

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
        return Comments.objects.filter(article_id = self.kwargs['article_pk'])
    
    
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
        
        
class LikeArticleViewSet(ModelViewSet):
    
    queryset = LikeArticle.objects.all()
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return LikeArticleSerializer
        
        if self.request.method == 'POST':
            return LikeAnArticleSerializer
        
        return LikeArticleSerializer
    
    def get_serializer_context(self):
        return {
            'user_id': self.request.user.id,
            'article_id': self.kwargs['article_pk']
        }
        

class DislikeArticleViewSet(ModelViewSet):
    
    queryset = DislikeArticle.objects.all()
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return DisLikeArticleSerializer
        
        if self.request.method == 'POST':
            return DisLikeAnArticleSerializer
        
        return DisLikeArticleSerializer
    
    def get_serializer_context(self):
        return {
            'user_id': self.request.user.id,
            'article_id': self.kwargs['article_pk']
        }