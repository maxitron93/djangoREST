from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from books.models import Book, Review
from books.api.serializers import BookSerializer, ReviewSerializer

# Using GenericAPIView class with mixins
# class BookListCreateAPIView(mixins.ListModelMixin,
#                             mixins.CreateModelMixin,
#                             generics.GenericAPIView):
#
#     queryset = Book.objects.all() # It's important that the variable name is 'queryset'
#     serializer_class = BookSerializer # It's important that the variable name is 'serializer_class'
#
#     # Override .get() method from GenericAPIView
#     def get(self, request, *args, **kwargs):
#         # Use the .list() method from ListModelMixing to create a new instance of the model
#         return self.list(request, *args, **kwargs)
#
#     # Override .post() method from GenericAPIView
#     def post(self, request, *args, **kwargs):
#         # Use the .create() method from CreateModelMixin to create a new instance of the model
#         return self.create(request, *args, **kwargs)


# Using Concrete View Class
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Using Concrete View Class
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # Override the method to customize what happens when creating a new Review instance
    def perform_create(self, serializer):
        book_pk = self.kwargs.get('book_pk')
        book = get_object_or_404(Book, pk=book_pk)
        serializer.save(book=book)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
