from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Each user can only have one profile
    bio = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username # username comes from the User model


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "statuses" # In the admin site, django will use the plural name. The default is to add an 's' at the end, so we need to define it ourself.

    def __str__(self):
        return str(self.user_profile)

