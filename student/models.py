from django.db import models

# Create your models here.
class Student(models.Model):
    student_roll= models.IntegerField(null=True)
    student_name= models.CharField( max_length=50,null=True)
    student_address= models.CharField( max_length=150,null=True)
    bookpricet= models.IntegerField(null=True)
    booktiti=models.CharField( max_length=254,null=True)


