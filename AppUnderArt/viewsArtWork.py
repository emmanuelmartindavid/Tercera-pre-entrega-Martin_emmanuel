from django.shortcuts import render, redirect
from AppUnderArt.models import ArtWork
from AppUnderArt.forms import SearchForm, ArtWorkForm


def search_artwork(request):
    mi_form = SearchForm(request.GET)
    if mi_form.is_valid():
        information = mi_form.cleaned_data
        filter_artworks = ArtWork.objects.filter(piece_name__contains=information['name'])
        context = {
            "artWorks": filter_artworks
        }
        return render(request, "AppUnderArt/search_artWork.html", context=context)


def create_artwork(request):
    if request.method == "POST":
        mi_form = ArtWorkForm(request.POST)

        if mi_form.is_valid():
            information = mi_form.cleaned_data
            artwork_save = ArtWork(
                piece_name=information['piece_name'],
                piece_author=information['piece_author'],
                piece_creation_year=information['piece_creation_year'],
            )
            artwork_save.save()
            return redirect("AppUnderArtArtWorks")
    context = {
        "form": ArtWorkForm()
    }
    return render(request, "AppUnderArt/create_artWork.html", context=context)


def edit_artwork(request, piece_name):
    get_artwork = ArtWork.objects.get(piece_name=piece_name)

    if request.method == "POST":
        mi_form = ArtWorkForm(request.POST)

        if mi_form.is_valid():
            information = mi_form.cleaned_data

            get_artwork.piece_name = information['piece_name']
            get_artwork.piece_author = information['piece_author']
            get_artwork.piece_creation_year = information['piece_creation_year']

            get_artwork.save()
            return redirect("AppUnderArtArtWorks")

    context = {
        "movie_name": piece_name,
        "form": ArtWorkForm(initial={
            "piece_name": get_artwork.piece_name,
            "piece_author": get_artwork.piece_author,
            "piece_creation_year": get_artwork.piece_creation_year,
        })
    }
    return render(request, "AppUnderArt/edit_artWork.html", context=context)


def delete_artwork(request, piece_name):
    get_artwork = ArtWork.objects.get(piece_name=piece_name)
    get_artwork.delete()
    return redirect("AppUnderArtArtWorks")


def artworks(request):
    all_artworks = ArtWork.objects.all()
    context = {
        "artworks": all_artworks,
        "search_form": SearchForm(),
    }
    return render(request, "AppUnderArt/artWorks.html", context=context)
