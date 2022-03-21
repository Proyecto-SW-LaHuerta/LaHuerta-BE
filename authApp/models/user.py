import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    username = models.CharField(max_length = 30, unique=True)
    password = models.CharField(max_length = 256)
    firstName = models.CharField(null=False, max_length=45)
    lastName = models.CharField(null=False, max_length=45)
    phoneNumber = models.BigIntegerField(null=True)
    birthday = models.DateField(null=False)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    status = models.BooleanField(default=False, null=False)

    def save(self, **kwargs):
        some_salt = "mMUj0DrIK6vgtdIYepkIxN"
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = "username"
