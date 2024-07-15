from django.urls import path
from core_app.views import core, core_detail

# localhost:8000/home
# localhost:8000/hpme/core

urlpatterns = [
    path('core/', core, name='core'),
    path('<int:core_id>/', core_detail, name='core_detail')
]
