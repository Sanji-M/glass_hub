from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render,redirect
from .forms import SignupForm

# My views
@login_required
def dashboard(request):
    if request.htmx:
        return render(request,'hub/_dashboard_content.html')
    return render(request,'hub/dashboard.html')

@login_required
def board_view(request):
    if request.htmx:
        return render(request, 'hub/_board_content.html')
    return render(request, 'hub/board.html')

@login_required
def settings_view(request):
    if request.htmx:
        return render(request, 'hub/_settings_content.html')
    return render(request,'hub/settings.html')

#signup view over here
# Handles post request and get request
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)  #form filled with data from the request
        
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            password1 = form.cleaned_data['password1']
            
         
            #blueprint for creating a user
            parts  = full_name.strip().split(' ',1)
            first_name = parts[0]
            last_name = parts[1] if len(parts) > 1 else ''
            username = full_name.lower().replace(' ', '_')  # Replace spaces with underscores for username

            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password1
            )

            login(request, user)  # Log the user in after successful signup
            return redirect('dashboard')  # Redirect to the dashboard after signup
    else:
        form = SignupForm()  

    return render(request,'hub/signup.html',{'form':form})
