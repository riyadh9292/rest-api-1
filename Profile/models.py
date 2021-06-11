from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models  import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Managers for user profile"""

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email')

        email = self.normalize_email(email) # Here normalize_email takes care of the second half
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self,email,name,password):
        """Creating a superuser"""
        user = self.model(
        email=self.normalize_email(email),
        name=name,
        password=password)

        user.set_password(user.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=50,unique=True)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name
    def get_short_name(self):
        """Retrive full name of user"""
        return self.name
    def __str__(self):
        """Return string representation of user"""
        return self.email
