from django.shortcuts import render
import requests
import json
from .forms import SearchForm

my_id = '11c1b02a6e96fc44d5bc2a59c0dcc332'

def home(request):

    # 검색 기능 (POST 요청)
    if request.method == "POST":
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key=' + my_id + '&query=' + searchword
            response = requests.get(url)
            movieData = response.text
            movie_list = json.loads(movieData)
            movie_list = movie_list['results']
            return render(request, 'search.html', {'movie_list': movie_list})

    # 메인 페이지의 최신 영화 목록 (GET 요청)
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + my_id
        response = requests.get(url)
        movieData = response.text
        movie_list = json.loads(movieData)
        movie_list = movie_list ['results']
        context = {'movie_list': movie_list, 'form': form}
        return render(request, 'index.html', context)


# 영화 정보 상세페이지
def detail(request, movie_id):
    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=' + my_id
    response = requests.get(url)
    movieData = response.text
    return render(request, 'detail1.html', {'movieData': movieData})
