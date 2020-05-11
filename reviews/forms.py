from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ( "title" , "content" )

# never include posted_when (auto update time in model class), user & book (user from requst.user and book from getObjector404 from book_id in create review function.)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( "content",)