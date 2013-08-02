from datetime import datetime, timedelta
from django.db import models

# Create your models here.
class Dog(models.Model):
    """ Dog class to keep track of all the dogs and their poop. """
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    bday = models.DateTimeField(blank=True, null=True)


class StoolManager(models.Manager):
    """ Stool manager """
    def increment_count(self, for_dog, increment_by=1):
        """ Increment the poop count for a dog """
        if not getattr(for_dog, "pk", None):
            dog, dog_created = Dog.objects.get_or_create(name=for_dog.lower(), age=6)
        else:
            dog = for_dog
        stool, created = self.get_or_create(dog=dog, defaults={"count": increment_by})
        if not created:
            stool.count += increment_by
            stool.save()
        return stool.count

        
class Stool(models.Model):
    """ Keep track of the poops that the dogs take """
    dog = models.ForeignKey('Dog')
    count = models.IntegerField(default=1, blank=True, null=True)
    objects = StoolManager()