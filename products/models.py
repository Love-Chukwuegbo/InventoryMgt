from django.db import models
from django.conf import settings
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser,PermissionsMixin
import uuid
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


class ProductCategory(models.Model):
    category_choices =  [("Battery"," Battery"),
    ("Brakepads","Brakepads"),
    ("Cleaner","Cleaner"),
    ("Coolant", " Coolant"),
    ("Filters", "Filters"),
    ("Linkages", "Linkages"),
    ("Lubricants",  "Lubricants"),
    ("Tires", "Tires")]
    category = models.CharField(max_length =50, choices = category_choices)
    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(ProductCategory, on_delete= models.CASCADE )
    image = models. ImageField(upload_to="profile/photos/", null =True, blank= True)
    Quantity =models.IntegerField()
    unit_price = models.IntegerField()
    unit_cost = models.IntegerField()
    sales_unit = models.IntegerField()
    sku =models.CharField(max_length=50, unique= True,blank=True)
    
    def save(self):
        if not self.sku:
            self.sku = str(uuid.uuid4()).replace('-', "" )[ :12]
            return super().save()
    def __str__(self):
        return self.name