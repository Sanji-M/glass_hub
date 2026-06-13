from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import SignupForm
# My views
@login_required
def dashboard(request):

    return render(request,'hub/dashboard.html')

#signup view over here
# Handles post request and get request
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)  #form filled with data from the request
        if form.is_valid():
            return render(request,'hub/login.html')


    else:

        return render(request,'hub/signup.html')
