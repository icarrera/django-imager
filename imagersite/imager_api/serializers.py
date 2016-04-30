from rest_framework import serializers
from imager_images.models import Photo

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Photo
        fields = ['user', 'image', 'title', 'description', 'date_uploaded', 'date_modified', 'published']
