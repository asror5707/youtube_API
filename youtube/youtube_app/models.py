from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    email= models.EmailField()
    def __str__(self):
        return self.ism

class Playlist(models.Model):
    nom = models.CharField(max_length=100)
    mijoz = models.ForeignKey(Mijoz,  on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nom

class Video(models.Model):
    nomi = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media/photo/', null=True)
    video = models.FileField(upload_to='media/video/', null=True,
    validators = [FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    date_uploaded = models.DateTimeField(auto_now_add=True)
    sourse = models.URLField(blank=True)
    duration = models.DurationField()
    playlist = models.ForeignKey(Playlist, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nomi


class Comment(models.Model):
    comments = models.TextField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz,on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    def str(self):
        return f"{self.mijoz},({self.comments})"

