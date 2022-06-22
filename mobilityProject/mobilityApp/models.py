from django.db import models

# Create your models here.

class CabUser(models.Model):

    userName = models.CharField(max_length=124*4, unique=True, blank=False)
    lastName = models.CharField(max_length=248*4, blank=False)
    emailAddress = models.EmailField(max_length=248*4, blank=False)
    phoneNumber = models.CharField(max_length=19*4, blank=False)
    hobbies = models.CharField(max_length=512*4, default="")
    validatedEmail = models.BooleanField(default=False)
    validatedNumber = models.BooleanField(default=False)
