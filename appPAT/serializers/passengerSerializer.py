from rest_framework import serializers
from appPAT.models.passenger import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id_passenger', 'name', 'document', 'email',
                  'password', 'birth_date', 'cellphone', 'gender']

    def create(self, validated_data):
        user_instance = Passenger.objects.create(**validated_data)
        return user_instance

    def to_representation(self, obj):
        user = Passenger.objects.get(id_passenger=obj.id_passenger)
        return {
            'id': user.id_passenger,
            'name': user.name,
            'password': user.password,
            'document': user.document,
            'email': user.email,
            'birth_date': user.birth_date,
            'cellphone': user.cellphone,
            'gender': user.gender
        }
