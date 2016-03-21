from rest_framework import serializers
from .models import ShowImage

class ShowImageSerializer (serializers.ModelSerializer):
    class Meta:
        model = ShowImage
        fields = ('id', 'image_name', 'image_url')