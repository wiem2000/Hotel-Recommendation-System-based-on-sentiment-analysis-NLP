from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotel_name=models.CharField(max_length=200)
    hotel_url=models.CharField(max_length=200)
    avg_rating=models.FloatField()
    image_url=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    def __str__(self):
        return self.hotel_name
    

class User(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    aspects=models.TextField()
    def __str__(self):
        return self.username