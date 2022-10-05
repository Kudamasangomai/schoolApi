from django.db import models
import random
from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your models here.


@receiver(post_save,sender=User)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)

def random_reg_number():
    return str(random.randint(1001,9999))

# Create your models here.

class students(models.Model):
    firstname = models.CharField(max_length=50,null=False,blank=False)
    lastname = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False,unique=True)
    regnumber = models.IntegerField(default=random_reg_number)
    date_created = models.DateTimeField(default=datetime.today)
 

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
