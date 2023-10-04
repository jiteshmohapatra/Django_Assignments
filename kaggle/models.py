from django.db import models

# Create your models here.

class software(models.Model):
    Id = models.IntegerField("Id",primary_key=True,null=False,blank=True)
    Rating = models.FloatField("Rating",null=True,blank=True)
    Company = models.CharField("Company",max_length=255,null=True,blank=True)
    Jobtitle =models.CharField("Jobtitle",max_length=255,null=True,blank=True)
    Salary = models.IntegerField("Salary",null=True,blank=True)
    Salariesreported = models.IntegerField("Salaryreported",null=True,blank=True)
    Location = models.CharField("Location",max_length=255,null=True,blank=True)
    Employmentstatus = models.CharField("Employmentstatus",max_length=255,null=True,blank=True)
    Jobroles = models.CharField("Jobroles",max_length=255,null=True,blank=True)

