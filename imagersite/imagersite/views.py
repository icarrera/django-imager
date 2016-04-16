# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from imager_images.models import Photo
from imager_profile.models import ImagerProfile
from django.contrib.auth import login, logout
from django.views.generic.detail import DetailView


def home_page(request):
    """Home page view."""
    try:
        img = Photo.objects.filter(published='public')[-1]
    except:
        img = '/media/static/krampus.jpg'
    return render(request, 'home.html', context={'img': img})


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'imager_images/templates/photo_detail.html'

class ProfileView(TemplateView):
    model = ImagerProfile
    template_name = 'user_profile.html'
