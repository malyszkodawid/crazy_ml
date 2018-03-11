"""crazy_ml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from web import views
from web import user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^change_password/$', views.change_password, name='password_change'),
    url(r'^info/$', views.index, name='info'),
    url(r'^descriptions/$', views.descriptions, name='descriptions'),
    url(r'^calendar/$', views.calendar, name='calendar'),

    url(r'^signup/$', views.signup, name='signup'),

    url(r'^write_json/$', views.write_json, name='write_json'),

    url(r'^sign_up/$', user.sign_up, name='login'),
    url(r'^login/$', user.login, name='login'),
    url(r'^retrieve_password/$', user.retrieve_password, name='password'),
    url(r'^password/$', user.password, name='password_change_post'),


    url('^events/$', views.events, name='events'),
    url('^event/(?P<event_id>\d+)/$', views.event, name='event_view'),

    url('^person/(?P<person_name>\w+)/$', views.person, name='person_view'),
]