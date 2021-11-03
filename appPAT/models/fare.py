from django.db import models
from .routeType import RouteType


class Fare (models.Model):
    id_fare = models.AutoField(primary_key=True)
    id_route_type = models.ForeignKey(RouteType, on_delete=models.CASCADE)
    fare = models.IntegerField(
        null=False, verbose_name='Fare')
    category_list = [('E', 'Economica'), ('J', 'Ejecutiva')]
    category = models.CharField(
        max_length=1, choices=category_list, default='E', verbose_name='Category', null=False)

    class Meta:
        db_table = 'fares'
        verbose_name = 'Fare'
        verbose_name_plural = 'Fares'
        ordering = ['id_fare']
