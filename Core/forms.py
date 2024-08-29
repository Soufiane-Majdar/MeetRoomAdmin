from django import forms
from .models import Reservation, BeverageOrder, Room

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'start_time', 'end_time', 'status']

class BeverageOrderForm(forms.ModelForm):
    class Meta:
        model = BeverageOrder
        fields = ['items', 'status']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'location', 'capacity', 'amenities']
