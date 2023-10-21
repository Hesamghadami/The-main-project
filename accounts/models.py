from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustumUser(AbstractUser):
    image = models.ImageField(upload_to='user', default='user.png')

    def __str__(self):
        return self.username

# Create your models here.

