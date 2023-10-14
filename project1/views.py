from rest_framework import generics
from rest_framework import status
from rest_framework.generics import RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Book, Author
from .serializer import BookSerializer, AuthorSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # @api_view(['GET'])
    # def books_api(request):
    #     books = Book.objects.all()
    #     serializer = BookSerializer(books, many=True)
    #     return Response(serializer.data)


class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = BookSerializer
    #     return Response(serializer.data)
    #


class AuthorCreate(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class DeleteBook(RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, id=None):

        try:
            book = Book.objects.get(id=id)
            serializer = self.get_serializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response(status=404, data={'message': 'Not found!'})


class DeleteAuthor(RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request, id=None):

        try:
            author = Author.oblects.get(id=id)
            serializer = self.get_serializer(author)
            return Response(serializer.data)
        except Author.DoesNotExist:
            return Response(status=404, data={'message': 'Not found!'})


class UpdateBook(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def retrieve(self, request, pk=None):
        try:
            book = Book.objects.filter(pk=pk).first()
            if book is not None:
                serializer = self.get_serializer(book)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Not found!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateAuthor(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def retrieve(self, request, pk=None):
        try:
            author = Author.objects.filter(pk=pk).first()
            if author is not None:
                serializer = self.get_serializer(author)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Not found!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
