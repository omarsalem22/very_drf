from blog.models import Post, Category
from rest_framework import generics, viewsets
from .serializers import PostSerializer, CategorySeroalizer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, AllowAny, BasePermission


class PostUserPermission(BasePermission):
    message = "Editing restrict to aithor only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(viewsets.ModelViewSet):

    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    
    def get_object(self,queryset=None, **kwargs):
        item=self.kwargs.get('pk')
        print(item)
        return get_object_or_404(Post,slug= item)
 
    def get_queryset(self):
        return Post.objects.all()


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
