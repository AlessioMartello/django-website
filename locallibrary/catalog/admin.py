from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

"""Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""

admin.site.register(Genre)
admin.site.register(Language)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass