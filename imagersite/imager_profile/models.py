"""Imager Profile model classes."""
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

PHOTO_CATEGORY = [
    ('portrait', 'Portrait'),
    ('nature', 'Nature'),
    ('sports', 'Sports'),
]

US_REGIONS = [
    ('pnw', 'Pacific Northwest'),
    ('ne', 'New England'),
    ('ma', 'Mid-Atlantic'),
    ('se', 'Southeast'),
    ('mw', 'Midwest'),
    ('ds', 'Deep South'),
    ('sw', 'Southwest'),
    ('cf', 'California'),
    ('ak', 'Alaska'),
    ('hi', 'Hawaii')
]


class ActiveUserManager(models.Manager):
    """Query Imager Profile attached to an active user."""

    def get_queryset(self):
        """Return query set of profiles with active users."""
        queryset = super(ActiveUserManager, self).get_queryset()
        return queryset.filter(user__is_active=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Profile attached to user model."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="profile",
                                on_delete=models.CASCADE,
                                )
    camera_model = models.CharField(max_length=255)
    location = models.CharField(max_length=3,
                                choices=US_REGIONS)
    photography_type = models.CharField(max_length=255,
                                        choices=PHOTO_CATEGORY)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name='friend_of')
    active = ActiveUserManager()
    objects = models.Manager()

    def __str__(self):
        """Return string output of username."""
        return self.user.get_full_name() or self.user.username

    @property
    def is_active(self):
        """Return a boolean value indicating if the profile's user is active."""
        return self.user.is_active
