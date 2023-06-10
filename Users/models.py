from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='/ProfilePics/default.jpg', upload_to='ProfilePics')
    home_address = models.CharField("Home Address", max_length=100)
    phone_number = models.CharField("Phone Number", max_length=20)
    latitude = models.FloatField("Latitude (Y)", validators=[MinValueValidator(-90), MaxValueValidator(90)]) # The latitude is limited within -90 to +90
    longitude = models.FloatField("Longitude (X)", validators=[MinValueValidator(-180), MaxValueValidator(180)]) # The longitude is limited within -180 to +18

    # Defining user's location and returning it as tuple for putting the location into map
    def userLocation(self):
            return (self.longitude, self.latitude)
    
    def __str__(self):
        return self.user.username