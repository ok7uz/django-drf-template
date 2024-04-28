from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.account.managers import UserManager


class User(AbstractUser):
    first_name = models.CharField(max_length=64, null=False, verbose_name='first name')
    last_name = models.CharField(max_length=64, null=False, verbose_name='last name')
    email = models.EmailField('email', unique=True, verbose_name='email')
    image = models.ImageField(upload_to="users/", verbose_name='image')

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
