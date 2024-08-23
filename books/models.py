from django.db import models

# Create your models here.
class Books(models.Model):
    book_title=models.CharField( max_length=225,null=True)
    book_auther= models.CharField(max_length=225,null=True)
    book_price=models.IntegerField(null=True)

    