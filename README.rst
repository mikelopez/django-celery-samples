Readme for celery-django-samples
------------------------------

Some sample code to illustrate the use of celery within a django project to execute periodic tasks related to your Django project.
This project demonstrates keeping track of how many times a dog creates a stool. It will process the dog via GET request and then increment the 
counter and send it off in a message. Every 'x' minutes, the task will fire off writing these objects to the database. 

Verifying the results
---------------------
Assuming a fresh database, In ``python manage.py shell`` you can run the following

.. code-block:: python

	from celeryapp.models import *
	for i in Dog.objects.all():
		len(i.get_stool_count())

Depending on how many times you sent the GET request from your browser or script, check for that number on the results of len() for each Dog

You can also Refer to the official documentation on how to get your project properly configured: http://docs.celeryproject.org/en/latest/getting-started/brokers/django.html
