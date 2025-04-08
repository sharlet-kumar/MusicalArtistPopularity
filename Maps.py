import googlemaps

class GoogleMapsClient:
    def __init__(self, api_key):
        self.client = googlemaps.Client(key=api_key)

    def get_location(self, latitude, longitude):
        #Reverse Geocoding based on latitude and longitude
        result = self.client.reverse_geocode((latitude, longitude))
        if result:
            #Return the full formatted address of the first result
            return result[0].get('formatted_address')
        return "Location not found"

if __name__ == "__main__":

    maps_api_key = 'secret'
    
    # Instantiate the GoogleMapsClient class with your API key
    maps_client = GoogleMapsClient(maps_api_key)
