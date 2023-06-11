from django.urls import path

from .views import *

urlpatterns = [
    path('', User_Profile, name='Profile'),
    path('login', Login, name='login'),
    path('signup', Signup, name='signup'),
    path('edit', edit_profile, name='edit_profile'),
    path('map', User_Map, name='map'),
]