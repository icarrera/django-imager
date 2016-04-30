from django.shortcuts import render
from rest_framework import mixins, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from imager_images.models import Photo
from imager_api.serializers import PhotoSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'photos': reverse('photo-list', request=request, format=format),
        'photodetail': reverse('photo-detail', request=request, format=format)
    })



class PhotoList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PhotoDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

