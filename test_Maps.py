import pytest
from googlemaps import Client
from Maps import GoogleMapsClient

def test_get_location_found():
    maps_api_key = 'secret'
    google_maps_client = GoogleMapsClient(maps_api_key)
    address = google_maps_client.get_location(37.7749, -122.4194)
    expected_address = "5911 US-101, San Francisco, CA 94103, USA"
    assert address == expected_address

def test_get_location_not_found():
    maps_api_key = 'secret'
    google_maps_client = GoogleMapsClient(maps_api_key)
    address = google_maps_client.get_location(0, 0)
    expected_address = "Location not found"
    assert address == expected_address
