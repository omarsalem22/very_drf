from django.urls import path
from .views import RegisterUserView,BlackListToken



urlpatterns = [
        path("register/",RegisterUserView.as_view(),name='register'),
        path('logout/blacklist/',BlackListToken.as_view(),name="logout")
        
]
