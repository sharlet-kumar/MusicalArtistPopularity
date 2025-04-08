from Team9Project import MusicDataDemo

def test_if_popular():
    artist = "Hozier"
    output = True
    expected_output = MusicDataDemo.is_artist_popular(artist)
    assert expected_output == output

def test_if_not_popular():
    Invalid_artist = 'blablada'
    output = False
    expected_output = MusicDataDemo.is_artist_popular(Invalid_artist)
    assert expected_output == output 

def test_if_on_tour():
    artist = "J. Cole"
    output = True
    expected_output = MusicDataDemo.is_on_tour(artist)
    assert expected_output == output

def test_if_not_on_tour():
    artist = "randomArtistNameWhoIsntOnTour"
    output = False
    expected_output = MusicDataDemo.is_on_tour(artist)
    assert expected_output == output


    

