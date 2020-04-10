from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from . import forms
from .models import Hotel_Details

def index(request):
    return render(request,'Managerapp/index.html')

def Add_hotel(request):
    form=forms.Hotel_form()
    if request.method=='POST':
        form = forms.Hotel_form(request.POST)
        if form.is_valid():
            post=form.save()
            return redirect('Manager_Index')
    return render(request,'Managerapp/hotel_form.html',{'form':form})

def Hotel_list(request):
    hotel_dict=Hotel_Details.objects.order_by('max_rooms')
    return render(request,'Managerapp/hotel_list.html',{'hotel':hotel_dict})

def Update(request, pk):
    """try:
        hotel = Hotel_Details.objects.get(pk=pk)
    except Book.DoesNotExist:
        return redirect('Manager_Index')"""
    hotel=get_object_or_404(Hotel_Details,pk=pk)
    if request.method == "POST":
        form = forms.Hotel_form(request.POST, instance=hotel)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.save()
            return redirect('Hotel_list')
    else:
        form = forms.Hotel_form(instance=hotel)
    return render(request, 'Managerapp/hotel_form.html', {'form': form})

def Delete(request, pk):
    try:
        hotel = Hotel_Details.objects.get(pk=pk)
    except Hotel_Details.DoesNotExist:
        return redirect('Hotel_list')
    hotel.delete()
    return redirect('Hotel_list')