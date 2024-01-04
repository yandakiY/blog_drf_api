from django.contrib import admin
from django.urls import path , include
from rest_framework_nested import routers
from . import views


routers = routers.DefaultRouter()
routers.register('categories' , views.CategoryViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , include(routers.urls))
    
]
