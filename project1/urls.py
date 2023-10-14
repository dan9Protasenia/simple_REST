from django.urls import path

from project1.views import BookList, BookCreate, \
    AuthorCreate, DeleteBook, DeleteAuthor, UpdateBook, UpdateAuthor

app_name = 'project1'

urlpatterns = [
    path('', BookList.as_view(), name='list'),
    path('create_book', BookCreate.as_view(), name='create_book'),
    path('create_author', AuthorCreate.as_view(), name='create_author'),
    path('delete_book/<int:pk>', DeleteBook.as_view(), name='delete_book'),
    path('delete_author/<int:pk>', DeleteAuthor.as_view(), name='delete_author'),
    path('update_book/<int:pk>', UpdateBook.as_view(), name='update_book'),
    path('update_author/<int:pk>', UpdateAuthor.as_view(), name='update_author'),
]
