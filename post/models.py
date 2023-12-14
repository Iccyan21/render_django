from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20,unique=True)
    photo = models.ImageField(upload_to='profile_images/',blank=True)
    video = models.FileField(upload_to='videos/')
    
class PostPhoto(models.Model):
    title = models.CharField(max_length=20,unique=True)
    photo = models.ImageField(upload_to='post_images/',blank=True)
    
class PostMovie(models.Model):
    postphoto = models.ForeignKey(PostPhoto, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=20,unique=True)
    video = models.FileField(upload_to='posts/')