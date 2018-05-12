
from django.db import models

# Create your models here.
from users.models import User
 
class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=100, unique=True, blank=False, null=False)
    releaseYear = models.CharField(max_length=100, unique=True, blank=False, null=False, default='N/A')
    casting = models.CharField(max_length=100, unique=True, blank=False, null=False, default='N/A')
    directors = models.CharField(max_length=100, unique=True, blank=False, null=False, default='N/A')
    producers = models.CharField(max_length=100, unique=True, blank=False, null=False, default='N/A')

    user = models.ForeignKey('users.User', related_name='movie', on_delete=models.CASCADE, null=False)
    class Meta:
        ordering = ('created',)
