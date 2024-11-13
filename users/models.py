from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name,first_name, password, **otherfields):

        otherfields.setdefault("is_staff", True)
        otherfields.setdefault("is_superuser", True)
        otherfields.setdefault("is_active", True)

        if otherfields.get("is_staff") is not True:
            raise ValueError(
                "Super user Must be assigned to is_staff=True "
            )
        if otherfields.get("is_superuser") is not True:
            raise ValueError(
                "Super user Must be assigned to is_superuser=True "
            )
        return self.create_user(email, user_name,first_name, password, **otherfields)

    def create_user(self, email, user_name,first_name, password, **otherfields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("Email Must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,first_name=first_name, **otherfields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email Address'),unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name=models.CharField(max_length=150,blank=True)
    start_data=models.DateTimeField(auto_now_add=True)
    about=models.TextField(_('about'),\
                           max_length=500,blank=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    objects=CustomAccountManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_name','first_name']
    
    def __str__(self) -> str:
        return self.user_name
    
    