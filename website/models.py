from django.db import models

# Create your models here.

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    rollNo = models.CharField(max_length=9)
    coming = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.rollNo}-{self.name}'
