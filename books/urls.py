
from django.contrib import admin
from django.urls import path, include
import books.views

urlpatterns = [
   
    path('', books.views.indexBooks, name="show_book_route"),
    path('authors/', books.views.authors, name="show_authors_route"),
    path("create", books.views.create_book),
    path("authors/create", books.views.create_author),
    path("update/<book_id>", books.views.update_book, name = 'update_book_route'),
    path("authors/update/<author_id>", books.views.update_author, name = "update_author_route"),
    path("delete/<book_id>", books.views.delete_book, name="delete_book_route"),
    path("authors/delete/<author_id>", books.views.delete_author, name="delete_author_route"),
    path("view/<book_id>", books.views.view_book_details, name = "view_book_details")

    
]
