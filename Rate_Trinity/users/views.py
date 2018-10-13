from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data.get('username')
            messages.success(request, f'Account succesfully created for { userName }.')
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form' : form})
