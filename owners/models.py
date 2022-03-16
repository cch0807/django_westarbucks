from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Owners(models.Model):
  name = models.CharField(max_length=45)
  email = models.CharField(max_length=300)
  age = models.IntegerField()

  class Meta:
    db_table = 'owners'

class Dogs(models.Model):
  owner = models.ForeignKey('Owners', on_delete=models.CASCADE, related_name='dogs')
  name = models.CharField(max_length=45)
  age = models.IntegerField()
  
  class Meta:
    db_table = 'dogs'