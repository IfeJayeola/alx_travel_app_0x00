from django.urls import path
from .views import (
    ListingListCreateView, ListingDetailView,
    BookingListCreateView, BookingDetailView
)

urlpatterns = [
    path('listings/', ListingListCreateView.as_view(), name='listings-list'),
    path('listings/<uuid:pk>/', ListingDetailView.as_view(), name='listing-detail'),

    path('bookings/', BookingListCreateView.as_view(), name='bookings-list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
]
