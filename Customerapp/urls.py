from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='Customer_Index'),
    path('hotel_page/',views.Show_hotels,name='Hotel_page'),
    path('booking_page/',views.Booking_page,name='Booking_page'),
]