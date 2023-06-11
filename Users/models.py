from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class UserProfile(models.Model):
    """
    Represents a user profile with additional information.

    Attributes:
        user (OneToOneField): The associated user object.
        email (EmailField): The email address of the user profile.
        profile_pic (ImageField): The profile picture of the user.
        home_address (TextField): The home address of the user.
        phone_number (CharField): The phone number of the user.
        latitude (FloatField): The latitude coordinate of the user's location.
        longitude (FloatField): The longitude coordinate of the user's location.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True)
    profile_pic = models.ImageField(default='/ProfilePics/default.jpg', upload_to='ProfilePics')
    home_address = models.TextField("Home Address")
    phone_number = models.CharField("Phone Number", max_length=20)
    latitude = models.FloatField("Latitude (Y)", validators=[MinValueValidator(-90), MaxValueValidator(90)]) # The latitude is limited within -90 to +90
    longitude = models.FloatField("Longitude (X)", validators=[MinValueValidator(-180), MaxValueValidator(180)]) # The longitude is limited within -180 to +18

    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name