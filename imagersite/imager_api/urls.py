from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from imager_api import views
from rest_framework.routers import DefaultRouter

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^api/$', views.api_root),
    url(r'^api/photos/$',
        views.PhotoList.as_view(),
        name='photo-list'),
    url(r'^api/photodetail/(?P<pk>[0-9]+)/$',
        views.PhotoDetail.as_view(),
        name='photo-detail'),
    # url(r'^albums/$',
    #     views.AlbumList.as_view(),
    #     name='album-list'),
    # url(r'^album/(?P<pk>[0-9]+)/$',
    #     views.AlbumDetail.as_view(),
    #     name='album-detail')
])

# router = DefaultRouter()
# router.register(r'photos'), views.PhotoViewSet)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]