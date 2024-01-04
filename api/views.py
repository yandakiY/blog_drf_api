from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from blog.models import Category , Article , Comments , UserBlog
from .serializers import CategorySerializer , CategoryCreateSerializer

# Create your views here.

class CategoryViewSet(ModelViewSet):
    
    queryset = Category.objects.all()
    
    def get_serializer_class(self):
        
        if self.request.method == 'GET':
            return CategorySerializer
        
        return CategoryCreateSerializer
