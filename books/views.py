from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
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

@login_required
def create_book(request):

    if request.method == "POST" :
        create_form=BookForm(request.POST)

        if create_form.is_valid():
            temporary_variable = create_form.save()
            messages.success(request, f"new book {temporary_variable.title} has been created")
            
            
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

@login_required
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

@login_required
def update_book(request, book_id):

    book_being_updated = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":

        book_form = BookForm(request.POST, instance=book_being_updated)
        if book_form.is_valid():
            book_form.save()
            return redirect(reverse(index))
        else:
            return render(request, "books/update.template.html", {
                "form" : book_form
            })


    else:
        book_form = BookForm(instance=book_being_updated)

        return render(request, "books/update.template.html", {
        "form": book_form
        })

@login_required
def update_author(request, author_id) :

    author_being_updated = get_object_or_404(Author, pk=author_id)

    if request.method == "POST":

        author_form = AuthorForm(request.POST, instance=author_being_updated)

        if author_form.is_valid():

            author_form.save()
            return redirect(reverse(authors))
        else:
            return render(request, 'books/update.template.html', {
            "form" : author_form
        })
    else:
        author_form = AuthorForm(instance=author_being_updated)

        return render(request, 'books/update.template.html', {
            "form" : author_form
        })



@login_required
def delete_book(request, book_id):

    book_to_delete = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        book_to_delete.delete()
        return redirect(index)
    else:
        return render(request, "books/delete_book.template.html", {
        "book" : book_to_delete
        })

@login_required
def delete_author(request, author_id) :

    author_to_delete = get_object_or_404(Author, pk=author_id)

    if request.method == "POST" :
        author_to_delete.delete()
        return redirect(authors)
    else: 

        return render(request, "books/delete_author.template.html", {
        "author" : author_to_delete
        } )