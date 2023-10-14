from django.contrib import admin

from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available_amount', 'author')
    list_display_links = ('name', 'price', 'available_amount', 'author')
    search_fields = ('name', 'price', 'available_amount', 'author')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_display_links = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
