from appPAT.models.flight import Flight
from appPAT.models.route import Route
from appPAT.models.plane import Plane
from appPAT.models.routeType import RouteType
from appPAT.models.fare import Fare
from appPAT.models.airport import Airport
from appPAT.serializers.airportSerializer import AirportSerializer
from rest_framework import serializers


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id_flight', 'route', 'plane', 'departure', 'arrival']

    def create(self, validated_data):
        route_data = validated_data.pop('route')
        plane_data = validated_data.pop('plane')
        fligh_instance = Flight.objects.create(**validated_data)
        Route.objects.create(**route_data)
        Plane.objects.create(**plane_data)
        return fligh_instance

    def to_representation(self, obj, category=None):
        route: Route = Route.objects.get(id_route=obj.id_route_id)
        plane: Plane = Plane.objects.get(id_plane=obj.id_plane_id)
        flight: Flight = Flight.objects.get(id_flight=obj.id_flight)
        route_type: RouteType = RouteType.objects.get(
            id_route_type=route.id_route_type_id)
        if category:
            fares = Fare.objects.filter(
                id_route_type=route_type.id_route_type, category=category)
        else:
            fares = Fare.objects.filter(
                id_route_type=route_type.id_route_type)

        return {
            'id_flight': flight.id_flight,
            'route': {
                'id_from': route.from_airport.id_airport,
                'from': route.from_airport.cod,
                'id_to': route.to_airport.id_airport,
                'to': route.to_airport.cod,
                'routeType': [{
                    'category': fare.category,
                    'fare': fare.fare
                } for fare in fares]
            },
            'plane': plane.plane_reference,
            'departure': flight.departure,
            'arrival': flight.arrival
        }
