from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='Manager_Index'),
    path('hotel_form/',views.Add_hotel,name='Hotel_form'),
    path('hotel_list/',views.Hotel_list,name='Hotel_list'),
    path('update/<int:pk>/', views.Update, name='Update'),
    path('delete/<int:pk>/',views.Delete,name='Delete'),
]