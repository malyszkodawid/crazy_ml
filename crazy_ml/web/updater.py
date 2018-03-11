from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from web.models import *
from sklearn.cluster import KMeans
import numpy as np


<<<<<<< HEAD
tag_dict = {
        'on_campus' : 0,
        'city_centre' : 1,
        'free' : 2,
        'talk' : 3,
        'dance' : 4,
        'alcohol' : 5,
        'food' : 6,
        'faculty' : 7,
        'susu' : 8,
        'movie' : 9,
        'play' : 10,
        'societies' : 11,
        'religion' : 12,
        'business' : 13,
        }

tag_size = len(tag_dict)



# set the number of clusters
def how_many_clusters(no_users):
    return round(no_users**(1/3))


# kmeans clustering
def kmeans(no_clusters, data):
    return KMeans(n_clusters=no_clusters, random_state=0).fit(data)


# for each cluster make the pearson correlation on their scores
def make_map(users, k_means):    
    user_map = {}
    k = k_means.labels_
    zipped = zip(k, users)
    for label, user in zipped:
        if label not in user_map:
            user_map[label] = []
        user_map[label].append(user)   
    return user_map


def main_f(users, tags):
    no_users = len(users)
    no_clusters = how_many_clusters(no_users)
    k_means = kmeans(no_clusters, tags)
    user_map = make_map(users, k_means)
    #make_map(users,k_means)
    print(user_map)
    return user_map


def update_event_prior():
    events = Event.objects.all()
    for event in events:
        users = User.objects.all()
        event_prior = sum([r.rating for r in Rating.objects.all() if r.event_id == event.id]) / len(users)
        
def update_similarities():
    users = User.objects.all()
    for u in users:
        if u.is_superuser:
            continue
        for v in [w for w in users if w.profile.cluster == u.profile.cluster and not(w.is_superuser)]:
            list_u = []
            list_v = []
            rated_events = [r.event_id for r in Rating.objects.all() if r.user_id == u.profile or r.user_id == v.profile] 
            for event in rated_events:
                if not Rating.objects.filter(user_id == u.profile, i_d == event.i_d).exists():
                    score = Rating.objects.get(user_id = u.profile, i_d = event.i_d)
                    list_u.append(score.rating)
                else:
                    list_u.append(0)
                if not Rating.objects.filter(user_id == v.profile, i_d == event.i_d).exists():
                    score = Rating.objects.get(user_id = v.profile, i_d = event.i_d)
                    list_v.append(score.rating)
                else:
                    list_v.append(0)
            sim = pearson_correlation(np.asarray(list_u), np.asarray(list_v))
            S = Similarity(user1_id = u.profile, user2_id=v.profile, similarity=sim)   
            S.save()
=======
def update_prior_event():
	pass
>>>>>>> d44b29b3c7424e648c2e94943d631da8bc62e285

# new function with events
    # events = list of events
    # scores = 2D list of scores for each event
    # for line in scores:
    #   calculate mean from the whole event
    #


def pearson_correlation(x, y):

	x = (x - np.mean(x)) / np.std(x)
	y = (y - np.mean(y)) / np.std(y)

	return np.dot(x, y) / len(x)


def event_score(user, sim_users, event):

	return np.mean([user_sim[(user, u)] * score[(u, event)] for u in sim_users]) 


@login_required()
@csrf_exempt
def update_clusters(request):
    user_tags = []
    users = User.objects.all()
    for u in users:        
        tag_vector = tag_size * [0]        
        tags = u.profile.tags.all()
        #print(tags)
        for t in tags:
            tag_vector[tag_dict[t.tag]] += 1        
        user_tags.append(tag_vector)
    #print(user_tags)
    user_map = main_f(users, np.asarray(user_tags))    
    # update field
    for c, users in user_map.items():
        for u in users:
            u.profile.cluster = c
            u.save()        
    update_similarities()
    

def update_prior_tags():
	 pass


def update_event_ratings():
	 pass


def update_24():
<<<<<<< HEAD
	 update_prior_tags()
	 update_user_similarities()
=======
	update_user_similarities()
>>>>>>> d44b29b3c7424e648c2e94943d631da8bc62e285


def update_1():
	 update_prior_event()
	 update_event_ratings()