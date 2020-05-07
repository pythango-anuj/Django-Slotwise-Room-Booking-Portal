from django.contrib.auth.forms import UserCreationForm
from django.forms import Form
from .models import Custom_User_Model

class RegistrationForm(UserCreationForm):
    class Meta:
        model=Custom_User_Model()
        fields=('user_type','username','first_name','last_name','email','password1','password2','gender','dob','contact_no','address')

