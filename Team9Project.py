from my_spotipy import SpotifyAPI
from FacebookApi import FacebookAPI
from LastFMAPI import LastFM
from TicketMaster import VenueFinder
from Maps import GoogleMapsClient
from YoutubeAPI import Youtube
from genius import GeniusAPI


class MusicDataDemo:
    
    @staticmethod
    def main(artist_name,Song_name,artist_num):
        LastFM_instance = LastFM()
        spotify_instance = SpotifyAPI('secret', 'secret')
        google_maps_api_key = 'secret'
        maps_client = GoogleMapsClient(google_maps_api_key)
        ticketmaster_api_key = 'secret'
        venue_finder = VenueFinder(ticketmaster_api_key, google_maps_api_key)
        facebook_api_key = 'secret'
        facebook_instance = FacebookAPI(facebook_api_key)
        genius_instance= GeniusAPI()
 
        print(f"Artist #{artist_num+1} of the day...\nYoutube Data:")
        print("Music Video Title:",  Youtube().get_top_music_videos_and_view_count()[artist_num]['title'])
        print("View Count:", Youtube().get_top_music_videos_and_view_count()[artist_num]['view_count'])
        print("Artist:", artist_name)
        print("Song Name:", Song_name) 
        print("\nArtist LastFM Data:\nBio: ", LastFM_instance.get_artist_bio(artist_name))
        print("\nLast FM Followers: ", LastFM_instance.get_artist_follower_count(artist_name))
        print("Album the Song is in:", LastFM_instance.get_album_name(Song_name, artist_name)) 
        print("Song listens on LastFM:", LastFM_instance.get_song_listens(Song_name, artist_name))
        print("\nFacebook Data:")
        page_id = facebook_instance.search_facebook_page(artist)  # Fix: Pass artist name to search_artist_page
        print("the artists facebook page is:" , page_id)
        if page_id:
            likes = facebook_instance.get_artist_likes(page_id)
            if likes is not None:
                print(f"The artist '{artist}' has {likes} likes on Facebook.")
            else:
                print(f"Failed to retrieve likes for the artist '{artist}'.")
        else:
            print(f"No Facebook Page found for the artist '{artist}'.")
        print("\nSpotify Data:\nSpotify Popularity: ", SpotifyAPI.get_popularity(spotify_instance,artist_name))
        print("Spotify Followers", SpotifyAPI.get_total_followers(spotify_instance,artist_name))
        print("\nGenius lyrics data:")
        print("Genius lyrics followers:", genius_instance.get_follower_count_GeniusAPI(Song_name))

            # Call VenueFinder for the current artist and print venues
        print("\nTicket Master Data: Venues and Maps Data: Locations:")
        venues = venue_finder.find_artist_venues(artist_name)  # Call the method with the artist name
        print(venues)
        print(MusicDataDemo.is_on_tour(artist_name))

        print("----------------------------------------------------------------------------------------")
   
    @staticmethod
    def is_artist_popular(artist,song_name): #this method takes in an artist name and checks to see if they can be considered popular
        LastFM_instance = LastFM()
        spotify_instance = SpotifyAPI('secret', 'secret')
        genius_instance= GeniusAPI()
        if SpotifyAPI.get_popularity(spotify_instance,artist) > 50 or (LastFM_instance.get_artist_follower_count(artist)> 10000 and genius_instance.get_follower_count_GeniusAPI(song_name)>1000):
            return True
        else:
            return False
    
    @staticmethod
    def is_on_tour(artist_name): #method that sees if artist has more than 5 tours which it will return true if it is
        ticketmaster_api_key = 'secret'
        google_maps_api_key = 'secret'
        venue_finder = VenueFinder(ticketmaster_api_key, google_maps_api_key)
        venue = venue_finder.find_artist_venues(artist_name)
        if venue_finder.get_venue_count() >4: #check to see if artist has more than 4 venues booked
            return "Artist is Currently on tour"
        else:
            return "Artist isn't performing or on tour or their tickets are not available through ticketmaster"
                

if __name__ == "__main__":
    youtube_instance = Youtube()  # Instantiate the Youtube class
    top_songs = youtube_instance.get_top_music_videos_and_view_count() #get top 10 music videos
    artist_names = youtube_instance.get_artist_names() #split the artist names from the title
    song_names = youtube_instance.get_song_names() #split the song names from the title
    
    counter = 0
    tour_counter = 0
    genius_counter=0
    for index, artist in enumerate(artist_names):
        MusicDataDemo.main(artist_names[index],song_names[index],index)  # Call main
        if MusicDataDemo.is_artist_popular(artist_names[index],song_names[index]) == True:
            counter += 1 
        if MusicDataDemo.is_on_tour(artist_names[index]) == "Artist is Currently on tour":
            tour_counter += 1
    print (f"Looking at the top 10 songs of the day, {counter} of the songs were from artists that would be considered to be of high popularity and {tour_counter} of those {counter} artists are on a tour or porforming a lot")