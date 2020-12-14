import requests
from pprint import pprint

with open('api_key.txt') as f:
    API_KEY = f.read()

def get_poster(movie_title):
    url = 'http://www.omdbapi.com/?t={}&apikey=6ce553d8'.format(movie_title, str(API_KEY))
    poster_url = eval(requests.get(url).text)['Poster']
    return poster_url
