"""Imager Profile model classes."""
from django.db import models
from django.conf import settings


class ActiveUserManager(models.Manager):
    """Query Imager Profile attached to an active user."""

    def get_queryset(self):
        """Return query set of profiles with active users."""
        queryset = super(ActiveUserManager, self).get_queryset()
        return queryset.filter(user__is_active__=True)


class ImagerProfile(models.Model):
    """Profile attached to user model."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="profile",
                                on_delete=models.CASCADE,
                                )
    camera_model = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    photography_type = models.CharField(max_length=255)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name='friend_of')
    active = ActiveUserManager()

    def __str__(self):
        """Return string output of username."""
        return self.user.get_full_name() or self.user.username

    @property
    def is_active(self):
        """Return a boolean value indicating if the profile's user is active."""
        return self.user.is_active
