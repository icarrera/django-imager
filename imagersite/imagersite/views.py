# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile
from django.contrib.auth import login, logout
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import ModelFormMixin
from django.core.exceptions import ImproperlyConfigured


def home_page(request):
    """Home page view."""
    try:
        img = Photo.objects.filter(published='public')[-1]
    except:
        img = '/media/static/krampus.jpg'
    return render(request, 'home.html', context={'img': img})


@method_decorator(login_required, name='dispatch')
class PhotoDetailView(DetailView):
    """Photo detail view."""
    model = Photo
    template_name = 'imager_images/photo_view.html'

    def get(self, request, *args, **kwargs):
        """Return photo if user owns photo."""
        photo = Photo.objects.filter(pk=kwargs['pk']).get()
        if (
            request.user == photo.user or
            photo.published == 'public' or
            (request.user in photo.user.friend_of.all() and
                photo.published == 'shared')
        ):
            return render(request, self.template_name, {'photo': photo})
        else:
            raise PermissionDenied

@method_decorator(login_required, name='dispatch')
class AlbumDetailView(DetailView):
    """Album detail view."""
    model = Album
    template_name = 'imager_images/album_view.html'

    def get(self, request, *args, **kwargs):
        try:
            album = Album.objects.filter(pk=kwargs['pk']).get()
        except ObjectDoesNotExist:
            raise HttpResponseNotFound('<h1>Page not found.</h1>')
        if (
            request.user == album.user or
            album.published == 'public' or
            (request.user in album.user.friend_of.all() and
                album.published == 'shared')
        ):
            return render(request, self.template_name, {'album': album})
        else:
            raise PermissionDenied

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    model = ImagerProfile
    template_name = 'user_profile.html'

@method_decorator(login_required, name='dispatch')
class CreatePhoto(CreateView):
    model = Photo
    template_name_suffix = '_create_form'
    fields = ['title', 'description', 'published', 'image']

    def form_valid(self, form, *args, **kwargs):
        """
        If the form is valid, save the associated model.
        """
        # import pdb; pdb.set_trace()
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()
        return super(CreatePhoto, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CreateAlbum(CreateView):
    model = Album
    template_name_suffix = '_create_form'
    fields = ['title', 'description', 'published', 'pictures', 'cover_photo']

    def get_form(self, form_class=None):
        """
        Returns an instance of the form to be used in this view.
        """
        # import pdb; pdb.set_trace()
        form = super(CreateAlbum, self).get_form()
        form.fields['pictures'].queryset = self.request.user.photo_set.all()
        return form

    def form_valid(self, form, *args, **kwargs):
        """
        If the form is valid, save the associated model.
        """
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()
        return super(CreateAlbum, self).form_valid(form)
