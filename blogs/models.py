from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustumUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title = models.CharField(max_length= 255)
    content = models.TextField()
    status = models.BooleanField(default=False)
    image1 = models.ImageField(upload_to= 'blog')
    image2 = models.ImageField(upload_to= 'blog')
    image3 = models.ImageField(upload_to= 'blog')
    client = models.ForeignKey(CustumUser, on_delete= models.CASCADE)
    client_url = models.CharField(max_length=255, default='#')
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

# Create your models here.
