from appPAT.models.fare import Fare
from rest_framework import serializers


class FareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fare
        fields = '_all_'
