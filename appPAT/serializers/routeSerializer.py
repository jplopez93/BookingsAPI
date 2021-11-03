from appPAT.models.route import Route
from rest_framework import serializers


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'
