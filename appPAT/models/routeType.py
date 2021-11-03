from django.db import models


class RouteType(models.Model):
    id_route_type = models.IntegerField(
        primary_key=True)
    name_route_type = models.CharField(
        max_length=20, unique=True, null=False, verbose_name='Route Type')

    class Meta:
        db_table = 'routetypes'
        verbose_name = 'Route_type'
        verbose_name_plural = 'Route_types'
        ordering = ['id_route_type']
