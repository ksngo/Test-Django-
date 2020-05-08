from django.db import models
from books.models import Book


# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length = 100 , blank=False)
    content= models.TextField(blank=False)
    posted_when = models.DateTimeField(blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)