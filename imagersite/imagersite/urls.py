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
from django.contrib.auth.views import login
from .views import home_page
# from .views import ClassView
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

# from django.conf import settings, static

# image_urls = []
# profile_urls = []
# urlpatterns = image_urls + album_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^home/(?P<id>[0-9]+)$', home_page, name='home_page'),
    url(r'^$', home_page, name='home_page'),
    # url('^', include('django.contrib.auth.urls')),
    # url(r'^login/$', login_view, name='login_view')
    # url(r'^home/(?P<id>[0-9]+)$', ClassView.as_view(), name='home_page')
    # url(r'^home/(?P<id>[0-9]+)$', TemplateView.as_view(template_name='home.html'), name='home_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
