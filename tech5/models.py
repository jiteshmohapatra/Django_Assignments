from django.db import models

# Create your models here.


class scholar(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()





class adit(models.Model):
    institute_name = models.TextField()
    country= models.TextField()
    establishment_date = models.DateField()

    

