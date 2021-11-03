from django.db import models


class Airport(models.Model):
    id_airport = models.AutoField(primary_key=True)
    cod = models.CharField(max_length=3, verbose_name='COD')
    name_airport = models.CharField(
        max_length=50, null=False, unique=True, verbose_name='Name Airport')
    city = models.CharField(max_length=30, null=False,
                            verbose_name='City')
    country = models.CharField(
        max_length=30, null=False, verbose_name='Country')

    class Meta:
        db_table = 'airports'
        verbose_name = 'Airport'
        verbose_name_plural = 'Airports'
        ordering = ['id_airport']
