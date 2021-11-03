"""proyectoPAT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from appPAT import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('passenger/', views.UserCreateView.as_view()),
    path('passenger/<int:pk>', views.UserDetailView.as_view()),
    path('passenger/update/<int:pk>', views.UserUpdateView.as_view()),
    path('flights/<int:user>', views.FlightsDatailView.as_view()),
    path('flights/filter/<int:user>/<int:from>/<int:to>/<str:month>/<int:year>',
         views.FlightsFilterView.as_view()),
    path('flights/<int:user>/<int:pk>', views.FlightDatailView.as_view()),
    path('booking/', views.BookingCreateView.as_view()),
    path('bookings/<int:user>', views.BookingsDetailView.as_view()),
    path('booking/<int:user>/<str:pnr>', views.BookingDetailView.as_view()),
    path('booking/update/<int:user>/<str:pk>',
         views.BookingUpdateView.as_view()),
    path('booking/remove/<int:user>/<str:pk>',
         views.BookingDeleteView.as_view()),
    path('airports/<int:user>', views.AirportsListView.as_view())
]
