from django.db import models
from django.utils import timezone

# Create your models here.
class MithilaModel(models.Model):
    # list of tuples where each tuple represents a region.
    # the first element of each tuple is a database representation and the second element is the human-readable name.
    MITHILA_REGION = [
        ('JNK', 'JANAKPUR'),
        ('SR', 'SIRAHA'),
        ('MTR', 'MAHOTTARI'),
        ('RJB', 'RAJBIRAJ'),
        ('BTR', 'BIRATNAGAR')
    ]
    place_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='mithilaimages/')
    # choices set to MITHILA_REGION to restrict the  possible values to those in the list.
    region = models.CharField(max_length=3, choices=MITHILA_REGION, default='JNK')

    # def __str__(self) -> str:
    #     return self.region
    
    def __str__(self) -> str:
        return self.get_region_display()  # This will return the human-readable name
    
    class Meta:
        ordering = ('place_name',)
        verbose_name_plural = "Mithila Models"