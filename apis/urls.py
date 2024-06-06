from django.urls import path
from .views import *

urlpatterns = [
    path('sam/', Home, name = 'initial loading'),
    path('sam2/', Home2, name = 'home2'),
    path('video_feed/', video_feed, name = 'video_feed'),
    path('report/', report, name='report'),
    
]