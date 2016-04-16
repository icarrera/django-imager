"""imagersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from .views import home_page
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
import registration


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home_page'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'redirect_field_name': 'home_page'}, name='logout'),
    url(r'^accounts/', include('registration.backends.hmac.urls'))

    # url('^', include('django.contrib.auth.urls')),
    # url(r'^home/(?P<id>[0-9]+)$', ClassView.as_view(), name='home_page')
    # url(r'^home/(?P<id>[0-9]+)$', TemplateView.as_view(template_name='home.html'), name='home_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
