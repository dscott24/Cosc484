from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
import uuid

class User(models.Model):
    user_id = models.UUIDField(primary_key=True,editable=False)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=40, unique=True)
    profile_img = models.ImageField()

class Thread(models.Model):
    name =  models.CharField(max_length=40)
    thread_ID = models.UUIDField(primary_key=True,editable=False)

class Message(models.Model):
    text = models.TextField()
    message_ID = models.UUIDField(primary_key=True, editable=False)
    user_ID = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField()
    thread_ID= models.ForeignKey(Thread, on_delete=models.PROTECT)
    date_time = models.DateTimeField()

class Member(models.Model):
    user_ID = models.ForeignKey(User, on_delete=models.PROTECT)
    thread_ID = models.ForeignKey(Thread, on_delete=models.PROTECT)



