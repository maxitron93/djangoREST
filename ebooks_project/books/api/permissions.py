from rest_framework import permissions

# Create new permission class by extending IsAdminUser class
class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    # Override has_permission method
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view) # Get is_admin from previous has_permission method (T/F)
        # Returns True if is_admin=True or if request.method is GET, HEAD, or OPTIONS (Safe methods)
        return request.method in permissions.SAFE_METHODS or is_admin

