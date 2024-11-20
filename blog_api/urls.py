from django.urls import path
from .views import PostList,CategoryList,CategortDetail,PostDetail,\
                   PostListDetailfilter,\
                   DeletePost,CreatePost,AdminDetail,EditPost
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path ("",PostList.as_view(),name='postlist'),
    path ("posts/",PostDetail.as_view(),name='PostDetail'),
    path("search/",PostListDetailfilter.as_view(),name="PostListDetailFilter"),
    path("admin/create/",CreatePost.as_view(),name="create"),
    path('admin/delete/<int:pk>/',DeletePost.as_view(),name='delete'),
    path("admin/edit/<int:pk>/",EditPost.as_view(),name='edit'),
    path("admin/detail/<int:pk>/",AdminDetail.as_view(),name='adminpostdetail')
    
    
]

