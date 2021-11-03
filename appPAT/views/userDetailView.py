from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from appPAT.models.passenger import Passenger
from appPAT.serializers.passengerSerializer import PassengerSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(
            algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            string_response = {'detail': 'Unauthorized Request'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(
            algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            string_response = {'detail': 'Unauthorized Request'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().put(request, *args, **kwargs)
