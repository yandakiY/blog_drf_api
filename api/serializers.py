from blog.models import Category , UserBlog , Article , Comments , ImageArticle
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer


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
        
class ArticleImageSerializer(ModelSerializer):
    
    class Meta:
        model = ImageArticle
        fields = ['id' , 'image']
        
class ArticleSerializer(ModelSerializer):

    user_author = UserCreateSerializer()
    category = CategorySerializer()
    images = ArticleImageSerializer(many=True)
    
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'slug',
            'subtitle',
            'description',
            'created',
            'like',
            'user_author',
            'category',
            'images'
        ]

class ArticleCreateSerializer(ModelSerializer):
    
    uploading_img = serializers.ListField(
        write_only = True,
        required = False,
        child = serializers.ImageField(max_length = 100000 , allow_empty_file = False , use_url = False)
    )
    
    class Meta:
        model = Article
        fields = [
            'category',
            'title',
            'subtitle',
            'description',
            'uploading_img',   
        ]
        
    def create(self, validated_data):
        # get upoloading image
        images = validated_data.pop('uploading_img')
        
        category = self.validated_data.get('category')
        title = self.validated_data.get('title')
        subtitle = self.validated_data.get('subtitle')
        description = self.validated_data.get('description')
        
        
        
        user_id = self.context['user_id']
        print('Id user' , user_id)
        # validated_data['user_author_id'] = user_id
        
        # create article without rn the image
        article_created = Article.objects.create(category_id = category.id , title = title , subtitle = subtitle , description = description , user_author_id = user_id)
        
        # Create a article_image
        for img in images:
            ImageArticle.objects.create(image = img , article = article_created)
        return article_created
    
    
class CommentsSerializer(ModelSerializer):
    
    user_author = UserCreateSerializer()
    article = ArticleCreateSerializer()
    class Meta:
        model = Comments
        fields = [
            'id',
            'comment',
            'article',
            'user_author'
        ]
        
        
class CommentsCreateSerializer(ModelSerializer):
    
    class Meta:
        model = Comments
        fields = [
            'comment'
        ]
        
    def create(self, validated_data):
        
        user_id = self.context['user_id']
        article_pk = self.context['article_id']
        comment = self.validated_data.get('comment')
        
        my_comment = Comments.objects.create(user_author_id = user_id , article_id = article_pk , comment = comment)
        return my_comment
        # return super().create(validated_data)