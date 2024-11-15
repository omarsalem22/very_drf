from blog.models import Post, Category
from rest_framework import generics
from .serializers import PostSerializer, CategorySeroalizer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated,AllowAny

class PostList(generics.ListCreateAPIView):

    permission_classes = [AllowAny]

    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [AllowAny]
    queryset = Post.postobjects.all()

    serializer_class = PostSerializer


class CategoryList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Category.objects.all()
    serializer_class = CategorySeroalizer


class CategortDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Category.objects.all()
    serializer_class = CategorySeroalizer
