from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    descriptions = models.TextField(default='')

    # def __str__(self) -> str:
    #     return self.region
    
    def __str__(self) -> str:
        return self.region()  # This will return the human-readable name
    
    class Meta:
        ordering = ('place_name',)
        verbose_name_plural = "Mithila Models"

    
# one to many relation
class MithilaFood(models.Model):
    mithilafoods = models.ForeignKey(MithilaModel, on_delete=models.CASCADE, related_name='mithilafoods')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foodrating = models.IntegerField()
    foodcomment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} food of {self.mithilafoods.place_name}'

  
# Many to many relation
class MithilaLanguage(models.Model):
    language_name = models.CharField(max_length=50)
    language_origin = models.CharField(max_length=50)
    mithila_place = models.ManyToManyField(MithilaModel, related_name='mithila_place')

    def __str__(self):
        return self.language_name
    

# One to one relaion
class MithilaCertificate(models.Model):
    mithila_certificate = models.OneToOneField(MithilaModel, on_delete=models.CASCADE, related_name='+')
    certificate_no = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.mithila_certificate.place_name}'