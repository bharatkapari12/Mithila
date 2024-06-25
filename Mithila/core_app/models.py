from django.db import models
from django.utils import timezone

# Create your models here.
class MithilaModel(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='mithilaimages/')
    