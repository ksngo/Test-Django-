from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "ISBN" , "desc")


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("First_Name", "Last_Name" , "Date_Of_Birth")