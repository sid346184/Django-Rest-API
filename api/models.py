from django.db import models

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
    



