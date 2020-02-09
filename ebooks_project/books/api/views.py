from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from books.models import Book, Review
from books.api.serializers import BookSerializer, ReviewSerializer
from rest_framework import permissions
from books.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from rest_framework.exceptions import ValidationError

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
    # Adding permissions to this specific endpoint
    permission_classes = [
        # permissions.IsAuthenticated
        IsAdminUserOrReadOnly # Custom permission class
    ]

# Using Concrete View Class
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Adding permissions to this specific endpoint
    permission_classes = [
        # permissions.IsAdminUser
        IsAdminUserOrReadOnly # Custom permission class
    ]

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    # Override the method to customize what happens when creating a new Review instance
    def perform_create(self, serializer):
        book_pk = self.kwargs.get('book_pk')
        book = get_object_or_404(Book, pk=book_pk)
        review_author = self.request.user

        review_queryset = Review.objects.filter(book=book,
                                                review_author=review_author)

        if review_queryset.exists():
            raise ValidationError('You Have Already Reviewed this Book!')
        else:
            serializer.save(book=book, review_author = review_author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        IsReviewAuthorOrReadOnly  # Custom permission class
    ]
