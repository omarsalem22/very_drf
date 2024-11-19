from django.urls import path
from .views import PostList,CategoryList,CategortDetail,PostDetail,PostListDetailfilter
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path ("",PostList.as_view(),name='postlist'),
    path ("posts/",PostDetail.as_view(),name='PostDetail'),
    path("search/",PostListDetailfilter.as_view(),name="PostListDetailFilter")
    
    
]

