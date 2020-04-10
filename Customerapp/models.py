from django.db import models
# Create your models here.
class Booking_details(models.Model):
    booking_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=100)
    age=models.IntegerField()
    booking_date=models.DateField()
    cin_time=models.TimeField()
    cout_time=models.TimeField()
    place_choice=models.CharField(max_length=20)


