from django.db import models

# Create your models here.
class employee(models.Model):
    id = models.IntegerField("EmpId",primary_key=True,unique=True,blank=True)
    empno = models.IntegerField("EmpNo",null=True,blank=True)
    firstname = models.CharField("FirstName",max_length=100,null=True,blank=True)
    lastname = models.CharField("LastName",max_length=100,null=True,blank=True)
    workdepartment = models.CharField("WorkDepartment",null=True,blank=True,max_length=100)
    phoneno= models.IntegerField("PhoneNo",null=True,blank=True)
    hiredate = models.DateField("HireDate",null=True,blank=True)
    birthdate = models.DateField("BirthDate",null=True,blank=True)
    salary = models.IntegerField("Salary",null=True,blank=True)
    bonus = models.DecimalField("Bonus",null=True,blank=True,max_digits=5,decimal_places=2)


