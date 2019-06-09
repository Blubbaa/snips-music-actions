#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
from spotify_controller import SpotifyController

# If this skill is supposed to run on the satellite,
# please get this mqtt connection info from <config.ini>
# Hint: MQTT server is always running on the master device
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class SpotifyPlayer(object):
	"""Class used to wrap action code with mqtt connection
		
		Please change the name refering to your application
	"""

	def __init__(self):
		self.spotify = SpotifyController()
		self.actions = {"pause":  self.spotify.pause, "play":  self.spotify.play, "next": self.spotify.next_track}
		
		# start listening to MQTT
		self.start_blocking()

	# --> Master callback function, triggered everytime an intent is recognized
	def master_intent_callback(self,hermes, intent_message):
		coming_intent = intent_message.intent.intent_name
		print('[Received] intent: {}'.format(intent_message.intent.intent_name))
		if coming_intent in self.actions
			self.actions[coming_intent]()
		
	# --> Register callback function and start MQTT
	def start_blocking(self):
		with Hermes(MQTT_ADDR) as h:
			h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
	SpotifyPlayer()
