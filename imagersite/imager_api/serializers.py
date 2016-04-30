from rest_framework import serializers
from imager_images.models import Photo
from django.contrib.auth.models import User

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Photo
        fields = ['user', 'image', 'title', 'description', 'date_uploaded', 'date_modified', 'published']

