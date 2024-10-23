from rest_framework import serializers

from blog.models import Post ,Category

class PostSerializer(serializers.ModelSerializer):
   class Meta:
        model=Post
        fields=('id',"title",'author','category','excerpt','content','status')

class CategorySeroalizer(serializers.ModelSerializer):

     class Meta:
      db_table = ''
      model=Category
      fields=('name',)
           
    