from django.shortcuts import render, HttpResponse, redirect
from .import models
from .forms import RegistrationForm
from django.contrib.auth import login,logout

# View for SIGN UP
def User_signup(request):
    return render(request,'Authentication/signup.html')

def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        form = RegistrationForm()
    return render(request, 'Authentication/signup.html')
'''def User_signup(request):
    if request.method == 'POST':
            if(user_type=='Manager'):
                return redirect('Manager_Index')
            elif(user_type=='Customer'):
                return redirect('Customer_Index')
            else:
                return HttpResponse('<h1>Choose Valid User Type</h1>')
        else:
            return HttpResponse("!!Invalid Credential!!<br>"
                            "your password can't be too similar to your other personal information.")
    return render(request, 'Authentication/signup.html', {'form': form})

'''
# View for Login
# REMAINING : Add message to on getting wrong data in login form.
def User_login(request):
    pass
'''
def User_login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if(user.user_position=='Manager'):
                return redirect('Manager_Index')
            elif(user.user_position=='Customer'):
                return redirect('Customer_Index')
        else:
            return HttpResponse('<h1> Please Fill the boxes carefully</h1>')
    else:
        form=AuthenticationForm()
    return render(request,'Authentication/login.html',{'form':form})
'''

# View for Logout
def User_logout(request):
    pass
'''
def User_logout(request):
    #user=request.user
    #logout(user)
    return redirect('Home')

'''