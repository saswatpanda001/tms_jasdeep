from django.contrib.auth import get_user_model
from users.models import UserProfileModel
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # Check if the profile already exists before creating a new one
    if created:
        # Only create a new profile if it doesn't already exist
        if not UserProfileModel.objects.filter(user=instance).exists():
            profile = UserProfileModel.objects.create(user=instance)
            profile.save()
            print("Profile created:", profile)
        else:
            print("Profile already exists for user:", instance)


@receiver(post_save, sender=UserProfileModel)
def update_user_last_name(sender, instance, **kwargs):
    user = instance.user
    if user.last_name != instance.role:
        user.last_name = instance.role
        user.save()
    