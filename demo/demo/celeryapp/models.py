from datetime import datetime, timedelta
from django.db import models

# Create your models here.
class Dog(models.Model):
    """ Dog class to keep track of all the dogs and their poop. """
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    bday = models.DateTimeField()

class Stool(models.Model):
    """ Keep track of the poops that the dogs take """
    TYPES_OF_POOP = (
            ('good', 'good'),
            ('moisty', 'moisty'),
            ('pretty solid', 'pretty solid'),
            ('muddy', 'muddy'),
            ('diarrhea for sure', 'diarrhea for sure'),
            ('bloody', 'bloody'),
            ('parasites', 'parasites'),
            ('an earplug', 'an earplug'),
    )
    type_of_poop = models.CharField(max_length=30, choices=TYPES_OF_POOP)
    date_taken = models.DateTimeField(default=datetime.now())
    dog = models.ForeignKey('Dog')
