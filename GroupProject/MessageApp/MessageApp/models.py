from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

class Message(models.Model):
    text = models.CharField('String', max_legnt)