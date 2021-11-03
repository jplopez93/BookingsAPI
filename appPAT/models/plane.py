from django.db import models


class Plane(models.Model):
    id_plane = models.AutoField(primary_key=True)
    plane_reference = models.CharField(
        max_length=45, null=False, verbose_name='Plane Reference')
    capacity = models.IntegerField(default=0, verbose_name='Capacity')

    class Meta:
        db_table = 'planes'
        verbose_name = 'plane'
        verbose_name_plural = 'planes'
        ordering = ['id_plane']
