from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

#class UserManager(BaseUserManager):
 #   def create_user(self, email, password):
#
 #       if not email:
  #        raise ValueError('The given email must be set')
   #     if not password:
    #        raise ValueError('User must set password')
#
 #       email = UserManager.normalize_email(email)
  #      base_user = self.model(email=email, is_active=True)
   #     base_user.set_password(password)
    #    
     #   return base_user
#user model overwritting the built in user model
#class User(AbstractBaseUser):
 #   user_id = models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4)
  #  email = models.EmailField(max_length=255, unique=True)
   # username = models.CharField(max_length=40, unique=True)
    #profile_img = models.ImageField(upload_to='profile_pictures', default='profile_pictures/None/default.png', null=True, blank=True)
    #is_active = models.BooleanField( default=True)                                    
    #USERNAME_FIELD = 'username'
    #REQUIRED_FEILDS = []
                                    
                                        

class Thread(models.Model):
    name =  models.CharField(max_length=40)
    thread_ID = models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4)

    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.TextField()
    message_ID = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='message_pictures', default='message_pictures/None/default.png', null=True, blank=True)
    thread_ID= models.ForeignKey(Thread, on_delete=models.PROTECT)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Member(models.Model):
    user_ID = models.ForeignKey(User,on_delete=models.CASCADE)
    thread_ID = models.ForeignKey(Thread, on_delete=models.PROTECT)

    def __str__(self):
        return self.thread_ID.name



