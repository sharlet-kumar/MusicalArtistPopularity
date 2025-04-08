from googleapiclient.discovery import build
import re
class Youtube:
    @staticmethod 
    def get_top_music_videos_and_view_count():
        
        api_key = "secret"
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Call the search.list method to retrieve the top 10 most popular music videos
        search_response = youtube.videos().list(
            part='snippet,statistics',
            chart='mostPopular',
            videoCategoryId='10',  # Video category ID for Music
            maxResults=10  
        ).execute()

        top10_music_videos = []

        # Iterate through the search results
        for video in search_response['items']:
            # Extract video information
            video_title = video['snippet']['title']
            video_id = video['id']
            video_views = video['statistics']['viewCount']
            top10_music_videos.append({'title': video_title, 'view_count': video_views})

        return top10_music_videos
    
    @staticmethod
    #Method to get the artist name from their 
    def get_artist_names():
        top10_music_videos = Youtube.get_top_music_videos_and_view_count()
        artist_names = []

        # Extract artist names from video titles
        for video in top10_music_videos:
            title = video['title']
            # Logic to extract artist name from title (assuming artist name is before '-' symbol)
            artist_name = re.split(r' - | – | "', title)[0] # splits it to leave only whats on the left
            delimiters = r'\s* x \s*|\s*ft\.\s*|\s* & \s*|,\s*|\s*\(|\s* feat.\s*|\s* – \s*|\s* feat \s*'#splits the feature and gets rid of them 
            split_artist_name = re.split(delimiters, artist_name, flags=re.IGNORECASE)[0].strip()
            artist_names.append(split_artist_name) 
        return artist_names
    
    @staticmethod
    def get_song_names(): # method to split the song name from the top 10 music videos
        top10_music_videos = Youtube.get_top_music_videos_and_view_count() #call method that gets top 10 music videos
        song_names = []

        for video in top10_music_videos:
            title = video['title']
            song_name = re.split(r' - | – | "', title)[-1] # returns the stuff on the right of the '-'
            delimiters = r'\s*\(\s*|\s*Offic|\s*ft\s*|\s* feat. \s*|\s* – \s*|\s* feat \s*'#Filter out the (official video) from the song name
            split_song_name = re.split(delimiters, song_name, flags=re.IGNORECASE)[0].strip()
            song_names.append(split_song_name)
        return song_names
    
