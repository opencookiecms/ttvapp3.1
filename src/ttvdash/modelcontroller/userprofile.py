from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    position = models.CharField(max_length=50, null=True, blank=True)
    supervision = models.CharField(max_length=50, null=True, blank=True)
    picture = models.CharField(max_length=50, null=True, blank=True)
    
    
    def __str__(self):
        return self.user.first_name

