from django.contrib import admin
from django.urls import path , include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('categories' , views.CategoryViewSet)
router.register('articles' , views.ArticleViewSet)


articles_router = routers.NestedDefaultRouter(router , 'articles' , lookup='article')
articles_router.register('comments' , views.CommentsViewSet , basename='article-comments')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , include(router.urls)),
    path('' , include(articles_router.urls))
    
]
