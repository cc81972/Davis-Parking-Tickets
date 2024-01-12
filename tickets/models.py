from django.db import models

# Create your models here.
class TicketInfo(models.Model):    
    location = models.CharField(max_length=200)
    date = models.DateTimeField(null=True)
    
    