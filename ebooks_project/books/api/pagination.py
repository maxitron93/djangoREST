from rest_framework.pagination import PageNumberPagination

# Create custom Pagination class by extending existing class
class SmallSetPagination(PageNumberPagination):
    # Set page_size for this existing class
    page_size = 1
