from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.

def homeView(request):
    return HttpResponse('Hello, World! Welcome to my Django Capstone')

class MenuItemViewSet(viewsets.ModelViewSet):
    """
    A viewset pertaining to the Menu Items
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    A viewset pertaining to the Table Booking schedule
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


