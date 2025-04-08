import pytest
from genius import GeniusAPI

def test_check_artist_follow_numbers_right():
    song_name= "love story"
    genius_instance= GeniusAPI()
    actual_output= genius_instance.get_follower_count_GeniusAPI(song_name)
    expected_output= 8673
    assert actual_output==expected_output

def test_check_song_does_not_exist():
    song_name="fedxghjblnk" #not a real song
    genius_instance= GeniusAPI()
    actual_output= genius_instance.get_follower_count_GeniusAPI(song_name)
    expected_output="No results found for the song."
    print(actual_output)
    assert actual_output== expected_output
    
def test_check_exception_handling():
    song_name= "#"
    genius_instance= GeniusAPI()
    actual_output= genius_instance.get_follower_count_GeniusAPI(song_name)
    expected_output= "Expected key ... not found in the data."
    assert actual_output== expected_output

