
from django.db import models

# Create your models here.
from users.models import User
 
class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    firstName = models.CharField(max_length=100, unique=True, blank=False, null=False)
    lastName = models.CharField(max_length=100, unique=True, blank=False, null=False, default='N/A')
    aliases = models.CharField(max_length=100, unique=True, blank=False, null=False, default='N/A')
    moviesAsActorActress = models.CharField(max_length=100, unique=True, blank=False, null=False, default='N/A')
    moviesAsDirector = models.CharField(max_length=100, unique=True, blank=False, null=False, default='N/A')
    moviesAsProducer = models.CharField(max_length=100, unique=True, blank=False, null=False, default='N/A')

    user = models.ForeignKey('users.User', related_name='person', on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ('created',)
