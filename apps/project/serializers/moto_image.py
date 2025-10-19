from rest_framework import serializers

from ..models import MotoImage


class MotoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotoImage
        fields = ("id", "image")
