from django.urls import path
from core_app.views import core

# localhost:8000/home
# localhost:8000/hpme/core

urlpatterns = [
    path('', core, name='core'),
]
