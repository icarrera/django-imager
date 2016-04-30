from django.shortcuts import render
from rest_framework import mixins, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from imager_images.models import Photo
from imager_api.serializers import PhotoSerializer
from rest_framework import viewsets
from imager_api.permissions import IsOwner


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'photos': reverse('photo-list', request=request, format=format),
        'photodetail': reverse('photo-detail', request=request, format=format)
    })


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsOwner, )

    def get_queryset(self):
        queryset = super(PhotoViewSet, self).get_queryset()
        return queryset.filter(user=self.request.user)
