from django import forms
from .models import Hotel_Details

class Hotel_form(forms.ModelForm):
    class Meta:
        model=Hotel_Details
        fields=['hotel_name','hotel_location','room_price','min_slot','max_rooms','before_days']