from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.db import models
import uuid


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):

        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(
            email,
            password,
            False,
            False,
            **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        return self._create_superuser(
            email,
            password,
            True,
            True,
            **extra_fields
        )


class User(AbstractUser):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    birthdate = models.CharField(max_length=10)
    is_admin = models.BooleanField()
    is_seller = models.BooleanField()
    is_active = models.BooleanField(default=True)
    address = models.OneToOneField(
        'address.Address', on_delete=models.CASCADE, related_name="user", null=True)
    username = models.CharField(unique=False, null=True, max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
