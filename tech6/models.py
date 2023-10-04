from django.db import models

# Create your models here.
class student(models.Model):
    regno = models.IntegerField("Regno",null=True,blank=True)
    name = models.CharField("Name",max_length=255,null=True,blank=True)
    state = models.CharField("State",max_length=255,null=True,blank=True)
    standard = models.IntegerField("Standard",null=True,blank=True)
    marks = models.IntegerField("Marks",null=True,blank=True)
