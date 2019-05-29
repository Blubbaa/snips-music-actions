from time import sleep
from spotify_controller import SpotifyController

spotify = SpotifyController()

spotify.play()
sleep(1)
spotify.pause()
sleep(1)
spotify.play()
sleep(1)
spotify.next_track()