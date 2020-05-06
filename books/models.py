from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title




class Author(models.Model):
    First_Name = models.CharField(blank=False, max_length=255)
    Last_Name = models.CharField(blank=False, max_length=255)
    Date_Of_Birth = models.CharField(blank=False, max_length=255)


    def __str__(self):
        return self.First_Name

class Book(models.Model) :
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.CharField)
    category = models.ForeignKey(Category, on_delete=models.CharField)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ManyToManyField(Author, blank=False)

    def __str__(self):
        return self.title