import requests

class GeniusAPI:
    def get_follower_count_GeniusAPI(self, song_name):
        token = "secret"

        search_term = song_name
        genius_search_url = f"https://api.genius.com/search?q={search_term}&access_token={token}"

        response = requests.get(genius_search_url)
        json_data = response.json()
        try:
            if json_data['response']['hits']:
                api_link = json_data['response']['hits'][0]['result']['primary_artist']['api_path']
                genius_artist_url = f"https://api.genius.com{api_link}?access_token={token}"
                response = requests.get(genius_artist_url)
                if response.status_code == 200:
                    json_data = response.json()
                    follower_count = json_data['response']['artist']['followers_count']
                    return follower_count
                else:
                    print("Failed to retrieve artist information.")
                    return "Failed to retrieve artist information."
            else:
                print("No results found for the song.")
                return "No results found for the song."
        except KeyError as e:
            print(f"Expected key {e} not found in the data.")
            return "Expected key ... not found in the data."
