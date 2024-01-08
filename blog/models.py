from django.db import models
from django.contrib.auth.models import AbstractUser , User , BaseUserManager
from django_extensions.db.models import TitleSlugDescriptionModel , TimeStampedModel,ActivatorModel
# Create your models here.
from django.utils.text import slugify
from core import settings
from utils.utils import ModelId



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class UserBlog(AbstractUser):
    
    username = None
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    

class Category(TitleSlugDescriptionModel , TimeStampedModel , ActivatorModel):
    
    def up(self, **kwargs):
        
        self.slug = slugify(self.slug)
        return super().save(**kwargs)
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        ordering = ['-id']
        

class Article(TitleSlugDescriptionModel , TimeStampedModel , ActivatorModel , ModelId):
    
    subtitle = models.CharField(max_length = 100 , blank = True , null = True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default = 1 , null = False , blank = False)
    image_article = models.ImageField(upload_to='media/', default='' , blank=True , null=True)
    user_author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE , default = 1)
    like = models.PositiveBigIntegerField(default = 0)

    @property
    def img(self):
        if self.image_article == '':
            self.image_article = ''
        
        return self.image_article
    
    # def like(self):
    #     self.like += 1
    #     self.save()
        
    
    # def unlike(self):
    #     self.like -= 1
        
    #     if self.like < 0:
    #         self.like = 0
        
    #     self.save()
    
    
    class Meta:
        ordering = ['-created']

class ImageArticle(models.Model):
    
    article = models.ForeignKey(Article , on_delete=models.PROTECT , related_name = 'images')
    image = models.ImageField(upload_to='media/', default='' , blank=True , null=True)


class LikeArticle(models.Model):
    
    article = models.ForeignKey(Article , on_delete=models.PROTECT , related_name = 'likes_article')
    user_author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)

  

class Comments(TimeStampedModel , ActivatorModel , ModelId):
    
    user_author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)
    article = models.ForeignKey(Article , on_delete=models.CASCADE , null = True , blank = True)
    comment = models.TextField(null = False , blank = False)