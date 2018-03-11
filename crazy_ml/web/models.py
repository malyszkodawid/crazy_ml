from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Group(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Faculty(models.Model):
    name = models.CharField(max_length=50, blank=False)
    text = models.TextField(max_length=1000, blank=True)


class School(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    text = models.TextField(max_length=1000, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles')
    is_male = models.BooleanField(default=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    customized = models.BooleanField(default=False)

    nationality = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s's profile" % self.user

    def gender_name(self):

        if self.is_male:
            return 'Male'

        return 'Female'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
