from LastFMAPI import LastFM

def test_artist_bio():
    input = "Hozier"
    output = 'Andrew Hozier-Byrne (born 17 March 1990), known mononymously as Hozier, is an Irish musician and singer-songwriter from Bray, County Wicklow, Ireland. In 2013 he released his debut EP, featuring the hit single "Take Me to Church", and his second EP "From Eden" in 2014. His debut studio album, "Hozier", was released in Ireland in September 2014 and globally in October 2014.\n\nHozier was born in Bray, County Wicklow, Ireland.  His mother is the visual artist Raine Hozier-Byrne (who also designed his latest album cover). <a href="https://www.last.fm/music/Hozier">Read more on Last.fm</a>'
    expected_output = LastFM.get_artist_bio(input)
    assert expected_output == output  

def test_artist_bio_artist_not_found():
    input = "Invalid_Artist"
    output = 'Error: The artist you supplied could not be found'
    expected_output = LastFM.get_artist_bio(input)
    assert expected_output == output

def test_album_name_found():
    song_input = "take me to church"
    artist_input = "Hozier"
    output = "Hozier"
    expected_output = LastFM.get_album_name(song_input, artist_input)
    assert expected_output == output 

def test_album_name_not_right_song_name():
    song_input = "InvalidSong"
    artist_input = "Hozier"
    output = 0
    expected_output = LastFM.get_album_name(song_input, artist_input)
    assert expected_output == output

def test_album_name_wrong_artist():
    song_input = "take me to church"
    artist_input = "InvalidArtist"
    output = 0
    expected_output = LastFM.get_album_name(song_input, artist_input)
    assert expected_output == output

def test_album_listens_Wrong_artistANDsong_Name():
    song_input = "InvalidSong"
    artist_input = "InvalidArtist"
    output = 0  
    expected_output = LastFM.get_album_name(song_input, artist_input)
    assert expected_output == output

def test_album_listens():
    song_input = "take me to church"
    artist_input = "Hozier"
    output = 17753926  #Number of listens as of March 30th (This value will need to change based on the listens)
    expected_output = LastFM.get_song_listens(song_input, artist_input)
    assert expected_output >= output

def test_album_listens_Wrong_Song_Name():
    song_input = "InvalidSong"
    artist_input = "Hozier"
    output = 'Error: Track not found'  
    expected_output = LastFM.get_song_listens(song_input, artist_input)
    assert expected_output == output

def test_album_listens_Wrong_artist_Name():
    song_input = "take me to church"
    artist_input = "InvalidArtist"
    output = 'Error: Track not found'  
    expected_output = LastFM.get_song_listens(song_input, artist_input)
    assert expected_output == output

def test_album_listens_Wrong_artistANDsong_Name():
    song_input = "InvalidSong"
    artist_input = "InvalidArtist"
    output = 'Error: Track not found'  
    expected_output = LastFM.get_song_listens(song_input, artist_input)
    assert expected_output == output

def test_artist_follower_count_right():
    artist_input = "Hozier"
    output = 2273590
    expected_output = LastFM.get_artist_follower_count(artist_input)
    assert expected_output >= output #takes into account the growing popularity of the artist (will fail if artist loses followers but thats unlikely)

def test_artist_follower_count_invalid_artist():
    artist_input = "InvalidArtist"
    output = 0
    expected_output = LastFM.get_artist_follower_count(artist_input)
    assert expected_output == output

