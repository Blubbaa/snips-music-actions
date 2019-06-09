import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyController(spotipy.Spotify):

	def __init__(self):
		#client_credentials_manager = SpotifyClientCredentials()
		#self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
		
		# this needs environment variables with spotify client id and secret
		# export SPOTIPY_CLIENT_ID='your-spotify-client-id'
		# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
		# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
		
		self.token = util.prompt_for_user_token('blubbaa92', 'user-modify-playback-state,user-read-playback-state,user-read-currently-playing')
		super().__init__(self.token)
		
	def pause(self):
		print('pause')
		self.pause_playback()
		
	def play(self):
		print('play')
		self.start_playback()