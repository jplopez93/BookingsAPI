from django.db import models
from .routeType import RouteType
from .airport import Airport


class Route(models.Model):
    id_route = models.IntegerField(primary_key=True, null=False)
    from_airport = models.ForeignKey(
        Airport, related_name='from_airport', on_delete=models.CASCADE, verbose_name='From')
    to_airport = models.ForeignKey(
        Airport, related_name='to_airport', on_delete=models.CASCADE, verbose_name='To')
    id_route_type = models.ForeignKey(
        RouteType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'routes'
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['id_route']
