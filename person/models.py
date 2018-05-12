
from django.db import models

# Create your models here.
from users.models import User
 
class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey('users.User', related_name='person', on_delete=models.CASCADE, null=False)
    class Meta:
        ordering = ('created',)
