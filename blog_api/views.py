from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from blog.models import Post, Category
from rest_framework import generics, viewsets
from .serializers import PostSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser 
from rest_framework import status
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, AllowAny, BasePermission


class PostUserPermission(BasePermission):
    message = "Editing restrict to aithor only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset=Post.objects.all() 

    # def get_queryset(self):
    #     user = self.request.user
    #     return Post.objects.filter(author=user)


class PostDetail(generics.ListAPIView):

    serializer_class = PostSerializer

    def get_queryset(self):

        slug = self.request.query_params.get('slug', None)
        return Post.objects.filter(slug=slug)


class PostListDetailfilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']


# Psot Admin

# class CreatePost(generics.CreateAPIView):

#     permission_classes = [IsAdminUser]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class CreatePost(APIView):
    
    # permission_classes=[IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser]
    
    def post(self,request,format=None):
        print(request.data)
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


    serializer_class = PostSerializer
class DeletePost(generics.RetrieveDestroyAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AdminDetail(generics.RetrieveAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EditPost(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    


    
    

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()  # Get the post instance
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
        
    #     if serializer.is_valid():
    #         serializer.save()  # Save the updated instance
    #         return Response(serializer.data)  # Return the updated data
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     permission_classes = [AllowAny]
#     queryset = Post.postobjects.all()

#     serializer_class = PostSerializer

#     def get_queryset(self):

#         slug = self.kwargs['pk']

#         return Post.objects.get(slug=slug)


class CategoryList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategortDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
