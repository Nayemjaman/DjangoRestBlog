from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save, post_delete, m2m_changed, pre_delete, pre_save, m2m_changed
from django.dispatch import receiver  # For post_delete and pre_delete signal.

# Create your models here.

class User(AbstractUser):
    is_member = models.BooleanField(default=False)
    is_craeator = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    def __str__(self) -> str: 	return self.user.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)# For when a user is created.
def create_auth_token(sender,instance=None,created=False,**kwags):
    if created:  
        Token.objects.create(user=instance)  

class Member(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='members') 
    gmail = models.EmailField(max_length=50, blank=True)

    def __str__(self) -> str: 	return self.user.username



class Creator(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='creators')
    gmail = models.EmailField(max_length=50, blank=True)
    joined_date = models.DateTimeField(auto_now_add=True) 

    def __str__(self) -> str: 	return self.user.username

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='staffs')
    gmail = models.EmailField(max_length=50, blank=True)
    joined_date = models.DateTimeField(auto_now_add=True) 
        
    def __str__(self) -> str: 	return self.user.username	






