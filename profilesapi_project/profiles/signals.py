from django.contrib.auth.models import User
from profiles.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

# This function will create a new Profile when ever a new User is created
# It's decorated using the @receiver decorator to denote that this function is a receiver
# This receiver accepts a post_save signal from a User sender
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(f'Created: {created}')
    if created:
        Profile.objects.create(user=instance)
