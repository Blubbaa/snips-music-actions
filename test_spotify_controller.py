import json
from time import sleep
from spotify_controller import SpotifyController

spotify = SpotifyController()

devices = spotify.devices()

for dev in devices['devices']:
	print(dev)
	if dev['is_active']:
		dev_id = dev['id']
		dev_name = dev['name']
		print(dev_id, dev_name)
spotify.play()
sleep(1)
spotify.pause()
# sleep(1)
# spotify.play()
# sleep(1)
# spotify.next_track()