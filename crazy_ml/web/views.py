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
    if request.user.last_login is None:
        return info(request)
    return render(request, 'dashboard.html', {})


@login_required()
@csrf_exempt
def calendar(request):
    return render(request, 'calendar.html', {})


@login_required()
@csrf_exempt
def descriptions(request):
    return render(request, 'descriptions.html', {'descriptions': Description.objects.filter(author=request.user)})


@login_required()
@csrf_exempt
def info(request):
    return render(request, 'questionnaire.html')


@login_required()
@csrf_exempt
def change_password(request):
    return render(request, 'password_change.html')


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
                    Tag.objects.create(tag=tag_name)
                    
            for ctg_name in event['category']:
                if not Category.objects.filter(category=ctg_name).exists():
                    Category.objects.create(category=ctg_name)
            

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
                
            #e.save()
                
                
