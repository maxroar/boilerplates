from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        messages.add_message(resuest, messages.ERROR, 'You were already logged in, goof. If you would like to log into or register a new account, please log out first.')
        print('logged in')
        return redirect('/success')
    return render(request, '/login_reg/index.html')
def success(request):
    return render(request, '/login_reg/success.html')
def register(request):
    # blahblahblah
    return redirect('/success')
