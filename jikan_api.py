import requests

def get_top_anime_titles():
    # make a request to the Jikan API to get the top anime
    response = requests.get('https://api.jikan.moe/v3/top/anime/1')

    # get the JSON data from the response
    data = response.json()

    # extract the anime titles from the JSON data
    anime_titles = [anime['title'] for anime in data['top']]

    # return the anime titles
    return anime_titles