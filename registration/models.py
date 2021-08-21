from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name   
        user.set_password(password)  # change password to hash
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")   

        user = self.model(
            email=self.normalize_email(email)
        )
        user.username = username
        user.phone = phone
        user.set_password(password)  # change password to hash
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


     
class User(AbstractBaseUser):
    username = models.CharField(max_length=20, verbose_name='username', null=True, blank=True, unique=True)
    email = models.EmailField(max_length=50)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    datebirth = models.CharField(max_length=50)
    date_joined = models.DateTimeField(verbose_name="date joined",  auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD="username"

    REQUIRED_FIELDS=['email', 'phone']

    objects=MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True