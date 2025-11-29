from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,Group,Permission
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    country = models.CharField(max_length=100,default="Unknown")
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_model',
        blank=True,
        verbose_name='groups',
        help_text='this model belongs to user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permission_set",
        blank=True,
        help_text='Spesific permission for only this user',
        verbose_name='user permission'
    )



    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['email', 'phone', 'country']  # теперь терминал спрашивает эти поля

   
class UserCreationManager(BaseUserManager):
    def create_user(self,username= None,password=None,email=None,**extra_fields):
        if not email:
            raise ValidationError("Email Must Added")
        email = self.normalize_email(email=email)
        user = self.model(
            username = username,
            email = email,
            **extra_fields
            
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self,username= None,password=None,email=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if not extra_fields.get('is_staff'):
            raise ValidationError('super user must be staff')
        if not extra_fields.get('is_superuser'):
            raise ValidationError('super user must be superuser')      
        return self.create_user(username=username,password=password,email=email,**extra_fields)
