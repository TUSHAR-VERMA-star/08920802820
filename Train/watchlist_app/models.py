from django.db import models

class Company(models.Model):
    companyName = models.CharField(max_length=100)
    ownerName = models.CharField(max_length=100)
    rollNo = models.CharField(max_length=20)
    ownerEmail = models.EmailField()
    accessCode = models.CharField(max_length=50)
