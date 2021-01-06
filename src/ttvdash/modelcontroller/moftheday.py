from django.db import models

class MessageOfTheday(models.Model):

    titlemessage = models.CharField(max_length=50, blank=True)
    MessageOfTheday = models.CharField(max_length=250, blank=True)
    postby = models.CharField(max_length=50, blank=True)
    timepost = models.CharField(max_length=10, blank=True)
    postimages = models.CharField(max_length=150, blank=True)
