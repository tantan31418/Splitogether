from django.db import models

# Create your models here.

class Group(models.Model):
    gname = models.CharField(max_length=50)
    group_id = models.CharField(max_length=50)

class User(Group):
    uid = models.CharField(max_length=50)
    uname = models.CharField(max_length=50)
    amount = models.IntegerField()