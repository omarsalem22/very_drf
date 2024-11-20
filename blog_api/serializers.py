from rest_framework import serializers
from blog.models import Post, Category

class PostSerializer(serializers.ModelSerializer):
    
    published = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'category', 'slug', 'excerpt', 'content', 'status','published')
        
        extra_kwargs = {
            'slug': {'required': False},
            'status':{'required':False}  ,
            # 'published':{'required':False}    
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
