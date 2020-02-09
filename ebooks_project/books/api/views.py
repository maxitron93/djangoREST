from rest_framework import generics
from rest_framework import mixins
from books.models import Book
from books.api.serializers import BookSerializer

class BookListCreateAPIView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):

    queryset = Book.objects.all() # It's important that the variable name is 'queryset'
    serializer_class = BookSerializer

    # Override .get() method from GenericAPIView
    def get(self, request, *args, **kwargs):
        # Use the .list() method from ListModelMixing to create a new instance of the model
        return self.list(request, *args, **kwargs)

    # Override .post() method from GenericAPIView
    def post(self, request, *args, **kwargs):
        # Use the .create() method from CreateModelMixin to create a new instance of the model
        return self.create(request, *args, **kwargs)

