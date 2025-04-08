
import pytest
from my_spotipy import SpotifyAPI

def test_get_popularity_existing_artist():
    spotify_api = SpotifyAPI(client_id="secret", client_secret="secret")
    popularity = spotify_api.get_popularity("Future")
    assert popularity > 0

def test_get_popularity_non_existing_artist():
    spotify_api = SpotifyAPI(client_id="secret", client_secret="secret")
    popularity = spotify_api.get_popularity("NonExistingArtist123")
    assert popularity == 0

def test_get_total_followers_existing_artist():
    spotify_api = SpotifyAPI(client_id="secret", client_secret="secret")
    followers = spotify_api.get_total_followers("Future")
    assert followers >= 0

def test_get_total_followers_non_existing_artist():
    spotify_api = SpotifyAPI(client_id="secret", client_secret="secret")
    followers = spotify_api.get_total_followers("NonExistingArtist123")
    assert followers == 0
