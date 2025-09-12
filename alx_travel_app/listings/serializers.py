from rest_framework import serializers
from .models import Listing
from .models import Booking

class ListingSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField()

    class Meta:
        model = Listing
        fields = '__all__'



class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    listing = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = "__all__"
