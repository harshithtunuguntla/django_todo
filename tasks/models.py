from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class tasks:
#     id:int
#     title:str
#     completed:bool
#     is_deleted:bool
#     priority:int
#     description:str
#     prev_priority:int


class tasks(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)  
    priority = models.CharField(max_length=200)
    description = models.TextField()
    prev_priority = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    username = models.CharField(max_length=200)
    number = models.IntegerField()


# class new(models.Model):
#     name = models.CharField(max_length=200)