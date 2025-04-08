import spotipy #importing spotify API called spotipy to use for interaction
from spotipy import Spotify

class SpotifyAPI: 
    def __init__(self, client_id, client_secret): #defining constructor for the SpotifyAPI class 
        self.sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyClientCredentials(client_id="secret", client_secret="secret")) #initliasing the spotify API client w client credentials 
  
    def get_popularity(self,artist_name): #method to get the popularity of an artist from Spotify 
        results = self.sp.search(q='artist:' + artist_name, type='artist')
        if results['artists']['items']:
            artist = results['artists']['items'][0]
            popularity = artist['popularity']
            return popularity
        else:
            return 0 #method returns 0 if the artist is not found 
  
    def get_total_followers(self, artist_name): #gets total followers of the artist from Spotify 
        results = self.sp.search(q='artist:' + artist_name, type='artist')
        if results['artists']['items']:
            artist = results['artists']['items'][0]
            followers = artist['followers']['total']
            return followers
        else:
            return 0 #returns 0 if the artist is not found 

#setting up spotify API credentials 
spotify_client_id = "secret"
spotify_client_secret = "secret"


#initalises Spotify API client 
spotify_api = SpotifyAPI(client_id=spotify_client_id, client_secret=spotify_client_secret)

#artist names retrieved from youtube API data 
artist_names = ['Future', 'Xavi', 'Future', 'iamcardib', 'Shakira', 'Olivia Rodrigo', 'LA PEOPLE II (Video Oficial)', 'Joyner Lucas']

#gets popularity and follower data for each artist 



