from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email,password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
   
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = ''
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.ImageField(default='avatar/avatar.png', upload_to='avatar/')
    birthday = models.DateField(auto_now_add=False)
    phone = models.CharField(max_length=12)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    jobstatus = models.CharField(max_length=255, blank=True, null=True)
    openToWork = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


    def __str__(self):
        return f'{self.name} {self.surname}'


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(default='avatar/avatarCompany.png', upload_to='avatar/')
    birthday = models.DateField(auto_now_add=False)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name