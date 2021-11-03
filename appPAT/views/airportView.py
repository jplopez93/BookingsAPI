from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from appPAT.models import Airport
from appPAT.serializers.airportSerializer import AirportSerializer


class AirportsListView(generics.ListAPIView):
    serializer_class = AirportSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(
            algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify=False)
        print("ARGUMENTOS KWARGS: ", self.kwargs)

        if valid_data['user_id'] != self.kwargs['user']:
            string_response = {'detail': 'Unauthorized Request'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Airport.objects.all().order_by('cod')
        return queryset
