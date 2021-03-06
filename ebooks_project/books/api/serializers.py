from rest_framework import serializers
from books.models import Book, Review

class ReviewSerializer(serializers.ModelSerializer):

    review_author = serializers.StringRelatedField(read_only=True) # Bind the request user to the author field

    class Meta:
        model = Review
        exclude = ('book',)

class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

