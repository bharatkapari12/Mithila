from django.urls import path
from auth.views import authpanel

# localhost:8000/home
# localhost:8000/hpme/core

urlpatterns = [
    path('', authpanel, name='authpanel'),
]
