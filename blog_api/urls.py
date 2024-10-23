from django.urls import path
from .views import PostList,CategoryList,PostDetail,CategortDetail



urlpatterns = [
    path("",PostList.as_view(),name="listcreate"),
    path("post_detail/<int:pk>",PostDetail.as_view(),name="post_detail"),

    path("categories", CategoryList.as_view(), name="categories"),
    path("category_detail/<int:pk>",CategortDetail.as_view(),name="category_detail"),


    

    
]
