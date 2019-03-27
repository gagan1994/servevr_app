from datetime import datetime
from django.db import models

class User(models.Model):
    id = models.IntegerField(max_length=10, blank=True, primary_key=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    last_login = models.DateTimeField(default=datetime.now())
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField(default=datetime.now(), blank=True)
