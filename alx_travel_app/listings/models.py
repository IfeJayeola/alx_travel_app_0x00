from django.db import models


# Create your models here.


class User(models.Model):
    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    ]

    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True
    )
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    passwordhash = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.firstname} {self.lastname} ({self.role})'

class Listing(models.Model):
    listing_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
        db_index= True)
    host_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=  models.CASCADE,
        related_name= 'listings')
    name = models.CharField(
        max_length = 30,
        null = False)
    description = models.TextField(
        null = False)
    location = models.CharField(
        max_length=225,
        null = False)
    pricepernight = models.DecimalField(
        max_digits= 10,
        decimal_places= 2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    review_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
        db_index = True)
    property_id = models.ForeignKey(
        'Listing',
        on_delete=models.CASCADE,
        related_name="reviews")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name= 'reviews')
    rating = models.IntegerField(
        validators= [MinValueValidator(1),MaxValueValidator(5)],)
    comment = models.TextField(),
    created_at = models.DateTimeField(auto_now_add= True)

class Bookings(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    room_id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Booking {self.booking_id} by User {self.user_id} for Room {self.room_id}"
