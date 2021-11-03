from appPAT.models.flight import Flight
from appPAT.models.passenger import Passenger
from appPAT.models.booking import Booking
from rest_framework import serializers
from .flightSerializer import FlightSerializer
from .passengerSerializer import PassengerSerializer
from appPAT.utils import MakePNR


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id_passenger', 'date_booking',
                  'coupon', 'id_flight', 'category']

    def create(self, validated_data):
        validated_data['pnr'] = MakePNR().pnr
        booking_instance = Booking.objects.create(**validated_data)
        return booking_instance

    def to_representation(self, obj):
        flight = Flight.objects.get(
            id_flight=obj.id_flight_id)
        passenger = Passenger.objects.get(id_passenger=obj.id_passenger_id)
        booking: Booking = Booking.objects.get(id_booking=obj.id_booking)
        return {
            'id_booking': booking.id_booking,
            'pnr': booking.pnr,
            'date_booking': booking.date_booking,
            'passenger': PassengerSerializer().to_representation(passenger),
            'coupon': booking.coupon,
            'flight': FlightSerializer().to_representation(flight, obj.category)
        }
