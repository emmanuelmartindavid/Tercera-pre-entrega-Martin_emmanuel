from django.shortcuts import render, redirect
from AppUnderArt.models import Book
from AppUnderArt.forms import BookForm, SearchForm


def home(request):
    return render(request, 'AppUnderArt/home.html')


def search_book(request):
    mi_form = SearchForm(request.GET)
    if mi_form.is_valid():
        information = mi_form.cleaned_data
        filter_books = Book.objects.filter(book_name__contains=information['name'])
        context = {
            "books": filter_books
        }
        return render(request, "AppUnderArt/search_book.html", context=context)


def create_book(request):
    if request.method == "POST":
        mi_form = BookForm(request.POST, request.FILES)

        if mi_form.is_valid():
            information = mi_form.cleaned_data
            book_save = Book(
                book_name=information['book_name'],
                book_author=information['book_author'],
                book_edition_year=information['book_edition_year'],
                book_image=information['book_image']
            )
            book_save.save()
            return redirect("AppUnderArtBooks")
    context = {
        "form": BookForm()
    }
    return render(request, "AppUnderArt/create_book.html", context=context)


def edit_book(request, book_name):
    get_book = Book.objects.get(book_name=book_name)

    if request.method == "POST":
        mi_form = BookForm(request.POST)

        if mi_form.is_valid():
            information = mi_form.cleaned_data

            get_book.book_name = information['book_name']
            get_book.book_author = information['book_author']
            get_book.book_edition_year = information['book_edition_year']

            get_book.save()
            return redirect("AppUnderArtBooks")

    context = {
        "book_name": book_name,
        "form": BookForm(initial={
            "book_name": get_book.book_name,
            "book_author": get_book.book_author,
            "book_edition_year": get_book.book_edition_year,

        })
    }
    return render(request, "AppUnderArt/edit_book.html", context=context)


def delete_book(request, book_name):
    get_book = Book.objects.get(book_name=book_name)
    get_book.delete()

    return redirect("AppUnderArtBooks")


def books(request):
    all_books = Book.objects.all()
    context = {
        "books": all_books,
        "search_form": SearchForm(),
    }
    return render(request, "AppUnderArt/books.html", context=context)
