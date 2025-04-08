import requests
from googlesearch import search

class FacebookAPI:
    def __init__(self, access_token):
        self.access_token = access_token

    @staticmethod
    def search_facebook_page(artist_name):
        # Perform a Google search for the artist's name with "Facebook" appended
        query = f"{artist_name} Facebook"
        try:
            search_results = search(query, num=5, stop=5, pause=2)  # Limiting to 5 results
            for url in search_results:
                if "facebook.com" in url:
                    # Extract page ID from the URL
                    page_id = url.split('/')[-2]
                    return page_id
        except Exception as e:
            print(f"An error occurred: {e}")
        
        return None

    def get_artist_likes(self, artist_id):
        url = f"https://graph.facebook.com/{artist_id}?fields=fan_count&access_token={self.access_token}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if 'fan_count' in data:
                return data['fan_count']
        except requests.exceptions.HTTPError as e:
            if response.status_code == 400:
                return None  # Return None instead of printing the error
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        return None
