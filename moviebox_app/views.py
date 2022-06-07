from django.shortcuts import render
import requests
import json

my_id = '11c1b02a6e96fc44d5bc2a59c0dcc332'

def home(request):
    url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + my_id
    response = requests.get(url)
    movieData = response.text
    obj = json.loads(movieData)
    obj = obj['results']
    return render(request, 'index.html', {'obj': obj})
