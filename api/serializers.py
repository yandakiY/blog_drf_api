from blog.models import Category , UserBlog , Article , Comments
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'created',
        ]
        
class CategoryCreateSerializer(ModelSerializer):
    
    name = serializers.CharField(source = 'title')
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]