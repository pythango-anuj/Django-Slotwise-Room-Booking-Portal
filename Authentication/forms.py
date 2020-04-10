from django.contrib.auth.forms import UserCreationForm
from .models import Custom_User_Model


class Manager(UserCreationForm):
    class Meta:
        model = Custom_User_Model
        fields={'username','email','user_position','first_name','last_name','password1','password2','contact_no'}
