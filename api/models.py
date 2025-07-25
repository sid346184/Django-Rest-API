from django.db import models
import datetime
# Create your models here.



class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    about=models.TextField(max_length=200)
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                  ('Hardware','Hardware'),
                                                  ('Service','Service'),
                                                  ))

    added_date=models.DateTimeField(auto_now=True)
    isActive=models.BooleanField(default=True)
    

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    position=models.CharField(max_length=50,choices=(('worker','worker'),
                                                     ('intern','intern'),
                                                     ('manager','manager'),
                                                     ('other','other')                                                    
                                                     ))
    about=models.TextField(max_length=200)
    added_date=models.DateField(default=datetime.date.today)
    
    company=models.ForeignKey(Company,on_delete=models.CASCADE)