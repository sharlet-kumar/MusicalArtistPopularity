
from YoutubeAPI import Youtube


def test_youtube_top_10_printing():
    output = 10
    expected_output = len(Youtube.get_top_music_videos_and_view_count())
    assert output == expected_output

def test_youtube_song_spliter(): # outputs 10 song names were just going to test to see if it splits the title
    input = 'Future : Future, Metro Boomin, Kendrick Lamar - Like That (Official Audio)' #not actually inputting this but this is what the title of the song is that will be split
    output = 'Like That'
    expected_ouput = Youtube.get_song_names()[0] #this will change depending on the day so it might not match 
    assert output == expected_ouput

def test_youtube_artist_name_spliter():
    input = 'Future : Future, Metro Boomin, Kendrick Lamar - Like That (Official Audio)' #not actually inputting this but this is what the title of the song is that will be split
    output = 'Future'
    expected_ouput = Youtube.get_artist_names()[0] # this will change depending on the day
    assert output == expected_ouput

def test_youtube_artist_doesnt_use_normal_title():
    input = 'Sexyy Red "Get It Sexyy" : Sexyy Red "Get It Sexyy" (Official Video)'
    output = 'Sexyy Red "Get It Sexyy"'# this will be the output as its not properly formatted (Nothing we can do about this)
    expected_ouptut = Youtube.get_artist_names()[2] #again this will change depending on the day
    assert output == expected_ouptut






     
      
