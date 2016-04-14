# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from imager_images.models import Photo
from django.contrib.auth import login, logout
from imager_images.models import Photo
from django.views.generic.detail import DetailView


def home_page(request):
    """Home page view."""
    try:
        img = Photo.objects.filter(published='public')[-1]
    except:
        img = '/media/static/krampus.jpg'
    return render(request, 'home.html', context={'img': img})


# def login_view(request):
#     return login(request)


# class ClassView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self):
#         try:
#             img = Photo.objects.all().order_by("?")[0]
#         except IndexError:
#             pass
#         return {'img': img}

# class-based views class example:
#
class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'imager_images/photo_detail.html'



def logout_view(request):
    logout(request)
    return redirect('homepage')
