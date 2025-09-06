from django.db import models
from django.conf import settings
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser,PermissionsMixin

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email = None, password = None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email addresss')
        user = self.model(
            username=username,
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, email= None, password = None, **extra_fields):
        extra_fields.setdefault ("is_staff" ,True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_staff = True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser = True.")
        if not extra_fields.get("is_active"):
            raise ValueError("Superuser must have is_active = True.")
        return self.create_user(username,email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()
    def __str__(self):
        return self.email
    
    
User = settings.AUTH_USER_MODEL