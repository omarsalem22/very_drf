from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post ,Category

class Test_Create_post(TestCase):
    @classmethod
    def setUpTestData(cls) :
        testcategory=Category.objects.create(name='django')
        testuser1=User.objects.create_user(username="aya",password='123456789')

