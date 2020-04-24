from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.URLField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name', 'image']
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Options(models.Model):
    name = models.CharField(max_length=30)
    value = models.BooleanField()

    class Meta:
        db_table = 'options'

    def __str__(self):
        return self.name


class Pushes(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    create_date = models.DateTimeField(auto_now_add=True)
    sent_date = models.DateTimeField()
    sent_status = models.BooleanField(default=False)
    sent_count = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'pushes'

    def __str__(self):
        return self.title
