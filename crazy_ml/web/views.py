import os
import json
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from web.models import *


@csrf_exempt
def index(request):
    if request.user.is_authenticated:
        return dashboard(request)

    return render(request, 'index.html')


@login_required()
@csrf_exempt
def dashboard(request):
    #if not request.user.profile.customized:
    #    return info(request)

    data = dict()

    events = Event.objects.all()
    data['main_recomendation'] = events[0]

    data['recomendations'] = events[1:5]

    users = User.objects.all()

    data['users'] = users[:6]

    data['events'] = events[5:11]

    return render(request, 'dashboard.html', data)


@login_required()
@csrf_exempt
def calendar(request):
    return render(request, 'calendar.html', {})


@csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')

    return render(request, 'signup.html', {})


@login_required()
@csrf_exempt
def descriptions(request):
    return render(request, 'descriptions.html', {'descriptions': Description.objects.filter(author=request.user)})


@login_required()
@csrf_exempt
def info(request):
    return render(request, 'questionnaire.html', )


@login_required()
@csrf_exempt
def change_password(request):
    return render(request, 'password_change.html')


@login_required()
@csrf_exempt
def events(request):
    data = {}
    data['events'] = Event.objects.all()
    return render(request, 'events.html', data)


@login_required()
@csrf_exempt
def event(request, event_id):
    data = {}
    data['event'] = Event.objects.get(pk=event_id)
    return render(request, 'event.html', data)


@login_required()
@csrf_exempt
def person(request, person_name):
    data = {}
    data['user'] = User.objects.get(username=person_name).profile

    return render(request, 'user.html', data)


@login_required()
@csrf_exempt
def write_json(requests):
    print(settings.STATICFILES_DIRS)
    path = os.path.join('..', settings.STATICFILES_DIRS[0],'data')
    for file in os.listdir(path):
        if file.endswith('.json'):
            json_data = json.load(open(os.path.join(path,file)))
            event = json.loads(json_data) 
            
            for tag_name in event['tags']:
                if not Tag.objects.filter(tag=tag_name).exists():
                    t = Tag(tag=tag_name)
                    t.save()
                    
            for ctg_name in event['category']:
                if not Category.objects.filter(category=ctg_name).exists():
                    c = Category(category=ctg_name)
                    c.save()
            

            e = Event(i_d = event['id'],
                      title = event['title'],
                      description = event['description'], 
                      start_date = event['start_date'],
                      end_date = event['end_date'],
                      place = event['place'],
                      organisers = event['organisers'],
                      web_link = event['web_link'],
                      tickets_link = event['tickets_link'])
            
            e.save()
            
            for tag_name in event['tags']:
                
                t = Tag.objects.get(tag=tag_name)
                e.tags.add(t)
                
            for ctg_name in event['category']:
                
                c = Category.objects.get(category=ctg_name)
                e.categories.add(c)
                
            e.save()


@login_required()
@csrf_exempt
def make_users(request):

    
    u = User(username = 'Niranjan')
    u.save()
    user_profile = u.profile  
    for tag_name in ['talk', 'movie', 'food', 'on_campus']:
        tag = Tag.objects.get(tag=tag_name)
        user_profile.tags.add(tag)
    user_profile.save()
    
    u = User(username = 'Tolis')
    u.save()
    user_profile = u.profile  
    for tag_name in ['talk', 'play', 'societies', 'movie', 'free']:
        tag = Tag.objects.get(tag=tag_name)
        user_profile.tags.add(tag)
    user_profile.save()
    
    u = User(username = 'Christian')
    u.save()
    user_profile = u.profile  
    for tag_name in ['talk', 'free', 'societies', 'dance', 'alcohol', 'food']:
        tag = Tag.objects.get(tag=tag_name)
        user_profile.tags.add(tag)
    user_profile.save()
    
    u = User(username = 'Yustina')
    u.save()
    user_profile = u.profile   
    for tag_name in ['alcohol', 'food', 'free','dance']:       
        tag = Tag.objects.get(tag=tag_name)
        user_profile.tags.add(tag)
    user_profile.save()
    
    u = User(username = 'Eirini')
    u.save()
    user_profile = u.profile  
    for tag_name in ['alcohol', 'food', 'free', 'movie', 'dance']:
        tag = Tag.objects.get(tag=tag_name)
        user_profile.tags.add(tag)
    user_profile.save()
    
    u = User(username = 'Aswin')
    u.save()
    user_profile = u.profile  
    for tag_name in ['talk', 'play', 'religion']:
        tag = Tag.objects.get(tag=tag_name)
        user_profile.tags.add(tag)
    user_profile.save()
    
    u = User(username = 'Shreevatsa')
    u.save()
    user_profile = u.profile  
    for tag_name in ['talk', 'play', 'societies']:
        tag = Tag.objects.get(tag=tag_name)
        user_profile.tags.add(tag)
    user_profile.save()
    
    
@login_required()
@csrf_exempt
def make_ratings(request):
    
    u = User.objects.get(username = 'Yustina').profile
    e = Event.objects.filter(i_d = '0')[0]
    r = Rating(user_id = u, event_id = e, rating = 10)
    r.save()
    
    u = User.objects.get(username = 'Yustina').profile
    e = Event.objects.filter(i_d = '4')[0]
    r = Rating(user_id = u, event_id = e, rating = 5)
    r.save()
    
    u = User.objects.get(username = 'Yustina').profile
    e = Event.objects.filter(i_d = '12')[0]
    r = Rating(user_id = u, event_id = e, rating = 2)
    r.save()
    
    u = User.objects.get(username = 'Yustina').profile
    e = Event.objects.filter(i_d = '26')[0]
    r = Rating(user_id = u, event_id = e, rating = -10)
    r.save()
    
    u = User.objects.get(username = 'Niranjan').profile
    e = Event.objects.filter(i_d = '30')[0]
    r = Rating(user_id = u, event_id = e, rating = 10)
    r.save()
    
    u = User.objects.get(username = 'Niranjan').profile
    e = Event.objects.filter(i_d = '20')[0]
    r = Rating(user_id = u, event_id = e, rating = 5)
    r.save()
    
    u = User.objects.get(username = 'Niranjan').profile
    e = Event.objects.filter(i_d = '11')[0]
    r = Rating(user_id = u, event_id = e, rating = -10)
    r.save()
    
    u = User.objects.get(username = 'Tolis').profile
    e = Event.objects.filter(i_d = '20')[0]
    r = Rating(user_id = u, event_id = e, rating = 10)
    r.save()
    
    u = User.objects.get(username = 'Tolis').profile
    e = Event.objects.filter(i_d = '32')[0]
    r = Rating(user_id = u, event_id = e, rating = -10)
    r.save()  