from django.shortcuts import render, redirect
from AppUnderArt.models import Movie
from AppUnderArt.forms import SearchForm, MovieForm


def search_movie(request):
    mi_form = SearchForm(request.GET)
    if mi_form.is_valid():
        information = mi_form.cleaned_data
        filter_movies = Movie.objects.filter(movie_name__contains=information['name'])
        context = {
            "movies": filter_movies
        }
        return render(request, "AppUnderArt/search_movie.html", context=context)


def create_movie(request):
    if request.method == "POST":
        mi_form = MovieForm(request.POST)

        if mi_form.is_valid():
            information = mi_form.cleaned_data
            movie_save = Movie(
                movie_name=information['movie_name'],
                movie_director=information['movie_director'],
                movie_release_year=information['movie_release_year'],
            )
            movie_save.save()
            return redirect("AppUnderArtMovies")
    context = {
        "form": MovieForm()
    }
    return render(request, "AppUnderArt/create_movie.html", context=context)


def edit_movie(request, movie_name):
    get_movie = Movie.objects.get(movie_name=movie_name)

    if request.method == "POST":
        mi_form = MovieForm(request.POST)

        if mi_form.is_valid():
            information = mi_form.cleaned_data

            get_movie.movie_name = information['movie_name']
            get_movie.movie_director = information['movie_director']
            get_movie.movie_release_year = information['movie_release_year']

            get_movie.save()
            return redirect("AppUnderArtMovies")

    context = {
        "movie_name": movie_name,
        "form": MovieForm(initial={
            "movie_name": get_movie.movie_name,
            "movie_director": get_movie.movie_director,
            "movie_release_year": get_movie.movie_release_year,
        })
    }
    return render(request, "AppUnderArt/edit_movie.html", context=context)


def delete_movie(request, movie_name):
    get_movie = Movie.objects.get(movie_name=movie_name)
    get_movie.delete()
    return redirect("AppUnderArtMovies")


def movies(request):
    all_movies = Movie.objects.all()
    context = {
        "movies": all_movies,
        "search_form": SearchForm(),
    }
    return render(request, "AppUnderArt/movies.html", context=context)
