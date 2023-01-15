from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework import permissions

# Create your views here.
def index(request: HttpRequest):
    return render(request, "index.html", {})


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(
    generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView
):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
