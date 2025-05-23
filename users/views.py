from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new User"""
    if request.method != 'POST':
        #Display blank registration form.
        form = UserCreationForm()
        return render(request, 'registration/register.html',{'form':form})
    else:
        #Process completed form
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            #Log the usger in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')
        
        #Display a blank or invalid form.
        context = {'form':form}
        return render(request, 'registration/register.html', context)

# Create your views here.
