from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Book, Author
from .forms import BookForm, AuthorForm

# Create your views here.
def index(request):

    books = Book.objects.all()
    return render(request,"books/index.template.html",{
        "books" : books
    })


def authors(request):

    authors = Author.objects.all()
    return render(request, "books/authors.template.html", {
        "authors" : authors
    })

def create_book(request):

    if request.method == "POST" :
        create_form=BookForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else: 
            return render(request, "books/create.template.html", {
                "form" : create_form
            })


    else: 
        create_form = BookForm()
        return render(request, "books/create.template.html", {
        "form" : create_form
        })


def create_author(request):

    if request.method == "POST":
        create_form = AuthorForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(authors)
        else:
            return render(request, "books/create.template.html", {
                "form" : create_form
            })

    create_form = AuthorForm()

    return render(request, "books/create.template.html", {
        "form": create_form
    })