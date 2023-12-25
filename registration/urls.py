from django.urls import path
from .views import register_participant
from .views import welcomeView

urlpatterns = [
    path('register/', register_participant, name='register_participant'),
    path('', welcomeView, name='welcome'),
]