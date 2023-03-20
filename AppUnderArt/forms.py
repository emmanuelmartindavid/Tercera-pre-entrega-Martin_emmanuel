from .models import Book, Movie, ArtWork
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'book_author', 'book_edition_year', 'book_image']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_name', 'movie_director', 'movie_release_year']


class ArtWorkForm(forms.ModelForm):
    class Meta:
        model = ArtWork
        fields = ['piece_name', 'piece_author', 'piece_creation_year']


class SearchForm(forms.Form):
    name = forms.CharField(max_length=40)
