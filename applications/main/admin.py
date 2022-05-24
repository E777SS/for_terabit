from django.contrib import admin

from . import models


class BooksInline(admin.TabularInline):
    model = models.Book
    list_display = [
        'title',
        'pages',
        'printed_date',
    ]
    extra = 0


@admin.register(models.Author)
class AuthorTemplateAdmin(admin.ModelAdmin):
    list_display = [
        'last_name',
        'get_books_count',
    ]
    list_filter = [
        'last_name',
    ]
    search_fields = [
        'last_name',
    ]
    inlines = [BooksInline]

    def get_books_count(self, obj):
        return len(obj.books.all()) if obj.books else 0

    get_books_count.short_description = 'Количество книг'
