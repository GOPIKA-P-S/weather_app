
from django.db import models
# Create your models here.

class Weather_Data(models.Model):
    city=models.CharField(max_length=300,verbose_name="City")
    timezone=models.DateTimeField(auto_now_add=True)
    temperature=models.FloatField()
    status=models.CharField(max_length=40)
    
    def __str__(self):
        return self.city



# class User(models.Model):
#     Username=models.CharField(max_length=200)
#     Email_id=models.EmailField(unique=True)
#     Password=models.CharField(max_length=100)
#     is_staff=models.BooleanField(default=True)

#     def __str__(self):
#         return self.Username
    




