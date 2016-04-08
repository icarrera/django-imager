# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from imager_profile.models import ImagerProfile
import logging

logger = logging.getLogger(__name__)
