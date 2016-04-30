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
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import registration
from .views import home_page, PhotoDetailView, CreatePhoto, AlbumDetailView, CreateAlbum, EditAlbum, EditPhoto, edit_profile
from imager_images.models import Photo, Album


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home_page'),
    url(r'^images/photos/add', CreatePhoto.as_view(success_url="/images/library/")),
    url(r'^images/albums/add', CreateAlbum.as_view(success_url="/images/library/")),
    url(r'^images/album/(?P<pk>\d+)/edit', EditAlbum.as_view(success_url="/images/library/")),
    url(r'^images/photos/(?P<pk>\d+)/edit', EditPhoto.as_view(success_url="/images/library/")),
    url(r'^profile/edit/$', edit_profile, name='edit_profile'),
    url(r'^images/photos/(?P<pk>\d+)$', PhotoDetailView.as_view()),
    url(r'^images/album/(?P<pk>\d+)$', AlbumDetailView.as_view()),
    url(r'^images/library/$', login_required(TemplateView.as_view(template_name='imager_images/library.html'))),
    url(r'^profile$', login_required(TemplateView.as_view(template_name='imager_profile/user_profile.html'))),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^api/', include('imager_api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
