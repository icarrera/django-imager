# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView


def home_page(request, *args, **kwargs):
    foo = 'garbanzo beans'
    return render(request, 'home.html', context={'foo': foo})

class ClassView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, id=1):
        foo = ' garbanzo beanz'
        return {'foo': foo}
