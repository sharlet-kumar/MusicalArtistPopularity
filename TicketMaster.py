import ticketpy
from Maps import GoogleMapsClient  

class VenueFinder:
    def __init__(self, api_key, maps_api_key):
        self.api_key = api_key
        self.tm_client = ticketpy.ApiClient(api_key)
        self.maps_client = GoogleMapsClient(maps_api_key)

    def find_artist_venues(self, artist_name):
        # Store venue information based on the artist's popularity
        venues_in_popular_country = {}
        venues_not_in_popular_country = {}

        output = f"Finding venues for {artist_name} ...\n"
        self.artist_venues = []  
        
        try:
            # Find events for the artist globally
            pages = self.tm_client.events.find(keyword=artist_name)
            country_counts = {}  # Using a dict for key(country) value(count) pairs
            
            for page in pages:
                for event in page:
                    if '_embedded' in event.json and 'venues' in event.json['_embedded'] and len(
                            event.json['_embedded']['venues']) > 0:
                        country = event.json['_embedded']['venues'][0].get('country', {}).get('name')
                        if country:
                            country_counts[country] = country_counts.get(country, 0) + 1

                            venue_name = event.json['_embedded']['venues'][0].get('name')
                            latitude = event.json['_embedded']['venues'][0]['location'].get('latitude')
                            longitude = event.json['_embedded']['venues'][0]['location'].get('longitude')

                            if venue_name and latitude is not None and longitude is not None:
                                venue = {
                                    'name': venue_name,
                                    'latitude': latitude,
                                    'longitude': longitude,
                                    'country': country
                                }
                                self.artist_venues.append(venue)

            if self.artist_venues:
                if country_counts:  # Check if country_counts is not empty
                    highest_popularity_country = max(country_counts, key=country_counts.get)
                    venues_in_popular_country[artist_name] = [v for v in self.artist_venues if
                                                            v['country'] == highest_popularity_country]
                    venues_not_in_popular_country[artist_name] = [v for v in self.artist_venues if
                                                                v['country'] != highest_popularity_country]
                else:
                    output += f"No country information found for {artist_name}\n"
            else:
                output += f"No events found for {artist_name}\n"

        except Exception as e:
            if str(e) == "'min'":
                output += f"No events found for {artist_name}\n"
                # Exception 'min' is caused when the country_counts dictionary is empty.
                # If the country counts dictionary is empty, there should not be any events for this artist.

        output += self.construct_output_string(venues_in_popular_country, venues_not_in_popular_country)
        # Return the output string
        return output

    def construct_output_string(self, venues_in_popular_country, venues_not_in_popular_country):
        # Construct the output string for venue locations
        output = "Venues in the highest popularity country:\n"
        for artist_name, venues in venues_in_popular_country.items():
            for venue in venues:
                location = self.maps_client.get_location(venue['latitude'], venue['longitude'])
                output += f"Venue: {venue['name']}, Location: {location}\n"

        output += "\nVenues not in the highest popularity country:\n"
        for artist_name, venues in venues_not_in_popular_country.items():
            for venue in venues:
                location = self.maps_client.get_location(venue['latitude'], venue['longitude'])
                output += f"Venue: {venue['name']}, Location: {location}\n"

        return output

    def get_venue_count(self):
        return len(self.artist_venues)


if __name__ == "__main__":
    api_key = 'secret'
    maps_api_key ="secret"
    artist_name = 'shakira'  
    venue_finder = VenueFinder(api_key, maps_api_key)

