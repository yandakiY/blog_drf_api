from django.contrib import admin
from django.urls import path , include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('categories' , views.CategoryViewSet)
router.register('articles' , views.ArticleViewSet)
router.register('likes' , views.LikeUserViewSet , basename='LikeUser')


articles_router = routers.NestedDefaultRouter(router , 'articles' , lookup='article')

articles_router.register('comments' , views.CommentsViewSet , basename='article-comments')
articles_router.register('like' , views.LikeArticleViewSet , basename='like-article')
articles_router.register('dislike' , views.DislikeArticleViewSet , basename='dislike-article')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , include(router.urls)),
    path('' , include(articles_router.urls)),
    # path('' , include(like_article_router.urls))
    
]
