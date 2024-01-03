from django.contrib import admin
from .models import UserBlog , Category , Article , Comments


# Register your models here.

@admin.register(UserBlog)
class UserBlogAdmin(admin.ModelAdmin):
    list_display = ['id' , 'email']
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'slug' , 'description' , 'created']
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'slug' , 'category' , 'description' , 'created']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user_author' , 'article' , 'created']