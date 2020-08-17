from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre

def index (request):
    # View function for the homepage of the site

    # Generate the counts for some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = "a")
    num_instances_available = BookInstance.object.filter(status_exact= "a").count()

    num_authors = Authors.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors
    }

    return render(request, "index.html", context=context)