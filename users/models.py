from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    realname = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'users'


