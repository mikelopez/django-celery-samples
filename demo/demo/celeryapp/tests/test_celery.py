""" 
Test celery 
"""

from django.test import TestCase
from demo.celeryapp.models import *
from celery.messaging import establish_connection
from kombu.compat import Publisher, Consumer
from termprint import *

class TestCelery(TestCase):

	def __send_message(self, item):
		""" Internal method to send a message """
		connection = establish_connection()
		publisher = Publisher(connection=connection, 
							  exchange="test_messages",
							  routing_key="test_increment_number",
							  exchange_type="direct")
		publisher.send(item)
		termprint("INFO", publisher)
		publisher.close()
		connection.close()
		return publisher


	def test_process_message(self):
		""" Test sending messages. Item will be dogs
		and I will count how many times they each 
		create a lovely stool. Scenario:
		 - Dopey will poop 5 times
		 - Jiggles will poop 7 times
		"""

		termprint("INFO", "Sending messages")
		dopey = [self.__send_message("dopey") for x in range(0,5)]
		jiggles = [self.__send_message("jiggles") for x in range(0,7)]

		connection = establish_connection()
		consumer = Consumer(connection=connection,
							queue="test_messages",
							exchange="test_messages",
							routing_key="test_increment_number",
							exchange_type="direct")
		clicks_for_item = {}
		messages_for_item = {}
		

		# save number of clicks for each 'item'
		termprint("ERROR", consumer)
		termprint("WARNING", dir(consumer))
		messages_count = 0
		for message in consumer.iterqueue():
			data = message.body
			messages_count += 1
			self.assertTrue(data)
			termprint("WARNING", dir(message))
			termprint("WARNING", "\n\tMessage body: %s" % data)
			clicks_for_item[data] = clicks_for_item.get(data, 0) + 1

			# store the message objects too so we can update them after
			if data in messages_for_item.keys():
				messages_for_url[data].append(message)
			else:
				messages_for_url[data] = [message]

			# display the information
			for item, click_count in clicks_for_item.items():
				#termprint("INFO", "\n%s has %s clicks" % item, click_count)
				# acknowledge the message
				[msgs.ack() for msgs in messages_for_item[item]]


		self.assertEquals(messages_count, 12)
		self.assertTrue("dopey" in clicks_for_item.keys())
		self.assertTrue("jiggles" in clicks_for_item.keys())
		self.assertTrue("dopey" in messages_for_item.keys())
		self.assertTrue("jiggles" in messages_for_item.keys())
		self.assertEquals(clicks_for_item.get("dopey"), 5)
		self.assertEquals(clicks_for_item.get("dopey"), 7)

		# queue should now be empty
		messages_queue2 = consumer.iterqueue()
		messages2_count = 0
		[messages2_count + 1 for i in messages_queue2]
		self.assertTrue(len(messages2_count) == 0)

		consumer.close()
		connection.close()





		




