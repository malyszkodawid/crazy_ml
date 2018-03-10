from django.db import models
from django.utils import timezone


class Group(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
