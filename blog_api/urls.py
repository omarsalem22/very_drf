from django.urls import path
from .views import PostList,CategoryList,PostDetail,CategortDetail
from rest_framework.routers import DefaultRouter

app_name="blog_api"

router=DefaultRouter()
router.register('',PostList,basename='postlist')

urlpatterns = router.urls

