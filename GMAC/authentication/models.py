from django.contrib.auth.models import AbstractUser
from django.db import models

# add models here.
class CustomUser(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)


