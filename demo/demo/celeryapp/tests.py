"""
Test the dog and stool models. 
"""

from django.test import TestCase
from models import *

class SimpleTest(TestCase):
    def __add_dogs(self):
        """ Internal helper to add dogs """
        dopey = Dog.objects.create(name="Dopey", age=6, bday=datetime(2007, 04, 16, 0,0,0))
        jiggles = Dog.objects.create(name="Jiggles", age=1, bday=datetime(2012, 12, 28, 0,0,0))

    def __delete_dogs(self):
        """ Internal helper to delete teh dogs after a test """
        for i in Dog.objects.all():
            i.delete()

    def test_dog(self):
        """ Test adding the dogs """
        self.__add_dogs()
        self.__delete_dogs()
    
    def test_stools(self):
        """ Test adding the stool records for the dogs """
        self.__add_dogs()
        dopey = Dog.objects.get(name='Dopey')
        jiggles = Dog.objects.get(name='Jiggles')
        self.assertTrue(dopey)
        self.assertTrue(jiggles)
        # add the stools
        yesterday = (datetime.now() - timedelta(days=1))
        today = datetime.now()

        dopey_yesterday = {'type_of_poop': 'moisty', \
                        'date_taken': yesterday, 'dog': dopey}
        dopey_today = {'type_of_poop': 'good', \
                        'date_taken': yesterday, 'dog': dopey}
        yesterdays_poop = Stool(**dopey_yesterday)
        yesterdays_poop.save()
        todays_poop = Stool(**dopey_today)
        todays_poop.save()
        yesterday_result = "Yesterday, %s took a poop and it was %s" % (\
                        dopey.name, yesterdays_poop.type_of_poop)
        today_result = "Today, %s took a poop and it was %s" % (\
                       dopey.name, todays_poop.type_of_poop)
        self.assertEquals(yesterday_result, \
                    "Yesterday, Dopey took a poop and it was moisty")
        self.assertEquals(today_result, \
                    "Today, Dopey took a poop and it was good")


        jiggles_yesterday = {'type_of_poop': 'earplug', \
                        'date_taken': yesterday, 'dog': jiggles}
        jiggles_today = {'type_of_poop': 'good', \
                        'date_taken': yesterday, 'dog': jiggles}
        yesterdays_poop = Stool(**jiggles_yesterday)
        yesterdays_poop.save()
        todays_poop = Stool(**jiggles_today)
        todays_poop.save()
        yesterday_result = "Yesterday, %s took a poop and it was %s" % (\
                        jiggles.name, yesterdays_poop.type_of_poop)
        today_result = "Today, %s took a poop and it was %s" % (\
                       jiggles.name,todays_poop.type_of_poop)
        self.assertEquals(yesterday_result, \
                    "Yesterday, Jiggles took a poop and it was earplug")
        self.assertEquals(today_result, \
                    "Today, Jiggles took a poop and it was good")

