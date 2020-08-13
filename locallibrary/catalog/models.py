from django.db import models

# Define the genre model
class Genre(models.Model):
    # Model representing the book genre
    name=models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        # String represnting the Model object
        return self.name

# Now define the book model
from django.urls import reverse

class Book(models.Model):
    # Model representing a book, but not an instances of it.
    title = models.CharField(max_length=200)
    # Author as a string because it hasnt been declared yet.
    # Foreign key because a book can have one author but an author can have many books.
    author = models.ForeignKey("author", on_delete=models.SET_NULL, null=True)
    summary =models.TextField(max_length=1000, help_text="Enter a brief description of the book.")
    isbn= models.CharField("ISBN", max_length=13,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # Books can have many genres and genres can have many books.
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book.")

    def __str__(self):
        # A string to represent the model object
        return self.title

    def get_absolute_url(self):
        # Returns a url to access a detailed record for this book
        return reverse("book-detail", args=[str(self.id)])

import uuid  # Required for unique book instances

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this book, in the library")
    book = models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS=(
        ("m" , "Maintenance"),
        ("o" , "On loan"),
        ("a" , "available"),
        ("r" , "reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default = "m",
        help_text="Book availability",
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f'{self.id} ({self.book.title})'

# Now author model

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True, blank=True)
    date_of_death=models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        # Returns a url to access a detailed record for this book
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        # String representing the Model object
        return f'{self.last_name} ({self.first_name})'

class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the original language of the book")

    def __str__(self):
        # A string to represent the model object
        return self.name