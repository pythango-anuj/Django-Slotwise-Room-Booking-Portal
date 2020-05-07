from django.urls import path,include
from .import views

urlpatterns = [
    path('sign_up/',views.User_signup,name='Signup'),
    path('',views.Register,name='Register'),
    path('_user_log_in/',views.User_login,name='Login'),
    path('',views.User_logout,name='Logout'),
    path('room_bookings/',include('Customerapp.urls'),name='Customer'),
    path('manage_bookings/',include('Managerapp.urls'),name='Manager'),
]
