from celery.messaging import establish_connection
from kombu.compat import Publisher, Consumer
from celeryapp.models import Dog, Stool

def send_increment_stool(dog):
	""" Send a message to increment the count """
		connection = establish_connection()
		publisher = Publisher(connection=connection,
							  exchange="dogstool", 
							  routing_key="increment_stool",
							  exchange_type="direct")
		publisher.send(dog)
		publisher.close()
		connection.close()

def process_stool(debug=False):
	""" Process all of the gathered increments by saving them 
	to the database. """
	connection = establish_connection()
	consumer = Consumer(connection=connection,
						queue="dogstool",
						exchange="dogstool",
						routing_key="increment_stool",
						exchange_type="direct")

	clicks_for_dog = {}
	messages_for_dog = {}
	for message in consumer.iterqueue():
		pass
		
