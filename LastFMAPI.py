import pylast
import requests
class LastFM:
    @staticmethod 
    def get_artist_bio(artist_name):
        my_API = pylast.LastFMNetwork(api_key='secret')
        try:
            # Get the artist object
            artist = my_API.get_artist(artist_name)
            bio = artist.get_bio_summary()
            return bio
        except pylast.WSError as e:
            return f"Error: {e}"
            
    @staticmethod
    def get_album_name(song_name, artist_name):
        base_url = "http://ws.audioscrobbler.com/2.0/"
        params = {"method": "track.getInfo","artist": artist_name,"track": song_name,"api_key": 'secret',"format": "json"
    }
        response = requests.get(base_url, params=params)
        data = response.json()
        if "track" in data and "album" in data["track"]:
            album_name = data["track"]["album"]["title"]
            return album_name
        else:
            return 0

    @staticmethod  #Method that returns the number of listens the song has on LastFM
    def get_song_listens(song_name, artist_name):
        try:
            network = pylast.LastFMNetwork(api_key='secret', api_secret='secret')
            track = network.get_track(artist_name, song_name) #gets track based on artist and song name
            if track:
                play_count = track.get_playcount() #get playcount
                return play_count
        except pylast.WSError as e:
            return f"Error: {e}"
        
    @staticmethod
    def get_artist_follower_count(artist_name):
        base_url = "http://ws.audioscrobbler.com/2.0/"
        params = {
            "method": "artist.getInfo",
            "artist": artist_name,
            "api_key": 'secret',
            "format": "json"
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if "error" in data: #if not found return an error message
            return 0
        else:
            artist_info = data["artist"]
            follower_count = artist_info["stats"]["listeners"] #get LastFm ollower count
            return int(follower_count) 
    
    
def main():
    artist_name = input("Please input an artist name: ")
    artist_song = input(f"Please enter a song by {artist_name}: ")
    print("Artist LastFM Data: Bio: ", LastFM.get_artist_bio(artist_name))
    print("Album the Song is in:", LastFM.get_album_name(artist_song, artist_name))
    print("Song listens on LastFM:", LastFM.get_song_listens(artist_song,artist_name))
    print("artist followers:", LastFM.get_artist_follower_count(artist_name))
    print(type(LastFM.get_artist_follower_count(artist_name)))
if __name__ == "__main__":
    main()

      