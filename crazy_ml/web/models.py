from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles')

    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s's profile" % self.user
