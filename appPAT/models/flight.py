from django.db import models
from .route import Route
from .plane import Plane


class Flight(models.Model):
    id_flight = models.AutoField(primary_key=True)
    id_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    id_plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    departure = models.DateTimeField(null=False, verbose_name='Departure')
    arrival = models.DateTimeField(null=False, verbose_name='Arrival')

    class Meta:
        db_table = 'flights'
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'
        ordering = ['id_flight']
