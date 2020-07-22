from django.shortcuts import render, HttpResponse, redirect
from .models import Custom_User_Model
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout

# View for SIGN UP
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
        else:
            return HttpResponse("invalid credential<br>"
                                "Your password can't be too similar to your other personal information")
    else:
        form = RegistrationForm
        args={'form':form}
        return render(request, 'Authentication/signup.html',args)

# View for Login
# REMAINING : Add message to on getting wrong data in login form.
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            cuser=Custom_User_Model.objects.get(username=username).user_type
            if str(cuser) == 'M':
                return redirect('Manager_Index')
            elif str(cuser) == 'C':
                return redirect('Customer_Index')
            else:
                return HttpResponse('<h1>Invalid User</h1>')
    return render(request,'Authentication/login.html')

# View for Logout
def logout_view(request):
    logout(request)
    message.info(request,"Logged Out Successfully.")
    return redirect("Home")