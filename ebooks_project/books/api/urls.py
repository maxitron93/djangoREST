from django.urls import path
from books.api.views import (BookListCreateAPIView,
                             BookDetailAPIView,
                             ReviewCreateAPIView,
                             ReviewDetailAPIView)

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='books_list'),
    path('books/<int:pk>', BookDetailAPIView.as_view(), name='book_details'),
    path('books/<int:book_pk>/review', ReviewCreateAPIView.as_view(), name='book_review'),
    path('reviews/<int:pk>', ReviewDetailAPIView.as_view(), name='review_detail'),
]