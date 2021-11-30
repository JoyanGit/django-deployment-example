from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class JoyanUserForm (forms.ModelForm):
    password = forms.CharField (widget= forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email', 'password')

class JoeUserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        # For some reason not able to install Pillow. So, Leaving profile pic field.
        fields = ('joy_profile_pic','joe_portfolio_site')

        # fields = ('joe_portfolio_site', )
