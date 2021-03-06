from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


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


class Tag(models.Model):
    tag = models.TextField(max_length=300, blank=True)
    
    
class Category(models.Model):
    category = models.CharField(max_length=100, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles')
    is_male = models.BooleanField(default=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    customized = models.BooleanField(default=False)
    
    cluster = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='tags')

    nationality = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s's profile" % self.user

    def gender_name(self):

        if self.is_male:
            return 'Male'

        return 'Female'

    def get_photo(self):

        if self.photo and hasattr(self.photo, 'url'):
            return self.image.url

        return 'static/images/user.png'
    
    def similar_users(self):
        users = User.objects.all()
        return [w for w in users if w.profile.cluster == self.cluster]
                   
    def top_scores(self):
        events_list = []
        for event in Event.objects.all():
            score = 0
            score += event.prior 
            for u in [v for v in User.objects.all() if self.cluster == v.profile.cluster]:
                if Rating.objects.filter(Rating.user_id == u.profile, Rating.event_id == event.i_d).exists():
                    score += Rating.objects.get(user_id = u.profile, event_id = event.i_d).rating * Similarity.objects.get(user1_id = self, user2_id = u.profile).similarity
            events_list.append((score, event))
        events_list.sort()
        return [e for (s, e) in events_list]
                        
                


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
    
class Event(models.Model):
    i_d = models.CharField(max_length=20, blank=False)
    title = models.TextField(max_length=250, blank=False)
    description = models.TextField(max_length=1000, blank=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    start_date = models.CharField(max_length=100, blank=True)
    end_date = models.CharField(max_length=100, blank=True)
    place = models.CharField(max_length=100, blank=True)
    organisers = models.CharField(max_length=250, blank=True)
    web_link = models.CharField(max_length=250, blank=True)
    tickets_link = models.CharField(max_length=250, blank=True)
    prior = models.FloatField(default = 0, blank=True)
    photos = models.CharField(max_length=250, blank=True)


class Rating(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(blank=False) 

    
class Similarity(models.Model):
    user1_id = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name = 'user1_id')
    user2_id = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name = 'user2_id')
    similarity = models.FloatField(default = 0, blank = True, null = True)