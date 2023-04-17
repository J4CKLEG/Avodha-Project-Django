from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # add any additional fields you need here
    # for example:
    phone_number = models.CharField(max_length=20)
