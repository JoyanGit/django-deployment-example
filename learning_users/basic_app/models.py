from django.db import models

# This is the user model class. It has user name and other properties of user.
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    # Note that User class already has all ifno needed for user. OneToOneField heps create a copy instea do inheriting it.
    # That is why the UserProfileInfo class didnt have User Class in its argument.
    user = models.OneToOneField (User,on_delete=models.CASCADE,)
    # Create Additional Fields
    joe_portfolio_site = models.URLField(blank=True)
    # For some reason not able to install Pillow. So, Leaving profile pic field.
    joy_profile_pic = models.ImageField ( upload_to = 'joyan_profile_pics', blank = True)

    # this is for sending user name if this class is called.
    def __str__(self):
        return self.user.username
