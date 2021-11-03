from appPAT.models.plane import Plane
from rest_framework import serializers


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'
