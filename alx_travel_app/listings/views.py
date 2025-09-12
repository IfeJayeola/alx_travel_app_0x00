from rest_framework import generics
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

# GET all listings or POST new one
class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

# GET single listing, PUT, DELETE
class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

# GET all bookings or POST new one
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# GET single booking, PUT, DELETE
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
