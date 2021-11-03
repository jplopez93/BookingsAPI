from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from appPAT.models.flight import Flight
from appPAT.models.route import Route
from appPAT.models.plane import Plane
from appPAT.models.routeType import RouteType
from appPAT.models.fare import Fare
from appPAT.serializers import FlightSerializer


class FlightsDatailView(generics.ListAPIView):
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        queryset = Flight.objects.all()
        return queryset


class FlightDatailView(generics.RetrieveAPIView):
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Flight.objects.all()

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)


class FlightsFilterView(generics.ListAPIView):
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request)
        print(self.kwargs)
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        queryset = Flight.objects.filter(
            id_route__from_airport=self.kwargs['from'],
            id_route__to_airport=self.kwargs['to'],
            departure__month=self.kwargs['month'],
            departure__year=self.kwargs['year'])
        print(queryset)
        return queryset
