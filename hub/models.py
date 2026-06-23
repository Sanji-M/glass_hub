from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to="tracks/")

    def __str__(self):
        return self.title

class TodoItem(models.Model):
    title=models.CharField(max_length=200)
    detail=models.CharField(max_length=100,blank=True,null=True)
    is_complete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='todos')

    def __str__(self):
        return self.title


class Suggestion(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True)
    icon = models.CharField(max_length=10, default="💡")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title