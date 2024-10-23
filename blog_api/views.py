from blog.models import Post,Category
from rest_framework import generics
from .serializers import PostSerializer,CategorySeroalizer

class PostList(generics.ListCreateAPIView):
    queryset=Post.postobjects.all()
    serializer_class=PostSerializer
    


class  PostDetail(generics.RetrieveUpdateDestroyAPIView):
       
       queryset=Post.postobjects.all()
       serializer_class=PostSerializer






class CategoryList(generics.ListCreateAPIView):
      
      queryset=Category.objects.all()
      serializer_class=CategorySeroalizer

class CategortDetail(generics.RetrieveUpdateDestroyAPIView):
      
      queryset=Category.objects.all()
      serializer_class=CategorySeroalizer  

    


