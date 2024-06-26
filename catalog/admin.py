from django.contrib import admin
from .models import Genre, Book, BookInstance, Author, Language

# Register your models here.
# admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
# admin.site.register(Language)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = (BookInstanceInline, )

class BookInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = (BookInline, )

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass