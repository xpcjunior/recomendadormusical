import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

class SpotifyApiService():
    
    def __init__(self) -> None:

        load_dotenv()
        
        self.id = os.getenv('spotify.dev.id')
        self.secret = os.getenv('spotify.dev.secret')

    
    def conectar(self):
        self.client_credentials_manager = SpotifyClientCredentials(
            client_id = self.id,
            client_secret = self.secret
        )

        self.client = spotipy.Spotify(
            client_credentials_manager = self.client_credentials_manager
        )
    
    def getTrack(self, id_musica):
        return self.client.track(id_musica)