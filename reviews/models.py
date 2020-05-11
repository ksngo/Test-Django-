from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from django.utils.timezone import now


# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length = 100 , blank=False)
    content= models.TextField(blank=False)
    posted_when = models.DateTimeField(blank=False, auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )

class Comment(models.Model):
    
    content = models.TextField(blank=False)
    posted_when = models.DateTimeField(blank=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, blank=True)