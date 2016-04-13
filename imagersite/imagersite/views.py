# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, logout, redirect
from django.views.generic import TemplateView
from imager_images.models import Photo



def home_page(request, *args, **kwargs):

    return render(request, 'home.html', context={})

class ClassView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        try:
            img = Photo.objects.all().order_by("?")[0]
        except IndexError:
            img = None
        return {'img': img}


    def logout_view(request):
        logout(request)
        return redirect('homepage')
