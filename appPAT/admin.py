from django.contrib import admin
from .models.airport import Airport
from .models.booking import Booking
from .models.fare import Fare
from .models.flight import Flight
from .models.passenger import Passenger
from .models.plane import Plane
from .models.route import Route
from .models.routeType import RouteType

# Register your models here.

admin.site.register(Airport)
admin.site.register(Booking)
admin.site.register(Fare)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Plane)
admin.site.register(Route)
admin.site.register(RouteType)
