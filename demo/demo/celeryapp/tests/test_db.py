"""
Test the dog and stool models. 
"""

from django.test import TestCase
from demo.celeryapp.models import *

class TestDatabases(TestCase):
    def __add_dogs(self):
        """ Internal helper to add dogs """
        dopey = Dog.objects.create(name="dopey", age=6, bday=datetime(2007, 04, 16, 0,0,0))
        jiggles = Dog.objects.create(name="jiggles", age=1, bday=datetime(2012, 12, 28, 0,0,0))


    def __delete_dogs(self):
        """ Internal helper to delete teh dogs after a test """
        for i in Dog.objects.all():
            i.delete()


    def test_dog(self):
        """ Test adding the dogs """
        self.__add_dogs()
        self.__delete_dogs()
    

    def test_increment_counter(self):
        """ Test adding the stool records for the dogs """
        self.__add_dogs()
        dopey = Dog.objects.get(name='dopey')
        jiggles = Dog.objects.get(name='jiggles')

        self.assertTrue(dopey)
        self.assertTrue(jiggles)

        # add the stools
        s = Stool.objects.increment_count(dopey.name)
        s2 = Stool.objects.increment_count(dopey.name)
        stool = Stool.objects.filter(dog=dopey)
        print "COUNT = %s" % stool[0].count
        self.assertTrue(stool[0].count == 2)


