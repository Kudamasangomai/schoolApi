from django.db import models
import random
# from datetime import datetime



def random_reg_number():
    return str(random.randint(1001,9999))

# Create your models here.

class students(models.Model):
    firstname = models.CharField(max_length=50,null=False,blank=False)
    lastname = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False,unique=True)
    regnumber = models.IntegerField(default=random_reg_number)
    date_created = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
