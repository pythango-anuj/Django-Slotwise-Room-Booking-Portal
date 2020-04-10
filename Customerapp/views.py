from django.shortcuts import render,HttpResponse
from Managerapp.models  import Hotel_Details

def index(request):
    return render(request,'Customerapp/index.html')

def Show_hotels(request):
    hotel_dict=Hotel_Details.objects.order_by('max_rooms')
    return render(request,'Customerapp/show_hotel.html',{'hotel':hotel_dict})

def Booking_page(request):
    return render(request,'Customerapp/booking_form.html')


