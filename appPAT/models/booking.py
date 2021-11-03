from re import M
from django.db import models
from .passenger import Passenger
from .flight import Flight


class Booking(models.Model):
    id_booking = models.AutoField(primary_key=True)
    id_passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    id_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    pnr = models.CharField(max_length=6, null=False, verbose_name='PNR')
    coupon = models.IntegerField(null=False, verbose_name='Coupon')
    category_list = [('E', 'Economica'), ('J', 'Ejecutiva')]
    category = models.CharField(
        max_length=1, choices=category_list, default='E', verbose_name='Category', null=False)

    date_booking = models.DateTimeField(
        auto_now_add=True, null=False, verbose_name='Date Booking')

    class Meta:
        db_table = 'bookings'
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        ordering = ['id_booking']
