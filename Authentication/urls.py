from django.urls import path,include
from .import views

urlpatterns = [
    path('register/',views.register,name='Register'),
    path('_user_log_in/',views.login_view,name='Login'),
    path('room_bookings/',include('Customerapp.urls'),name='Customer'),
    path('manage_bookings/',include('Managerapp.urls'),name='Manager'),
]
