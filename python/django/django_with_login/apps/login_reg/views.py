from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        messages.add_message(resuest, messages.ERROR, 'You were already logged in, goof. If you would like to log into or register a new account, please log out first.')
        print('logged in')
        return redirect('/success')
    return render(request, 'login_reg/index.html')
def register(request):
    errors = User.objects.validate_reg(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/')

    is_email = User.objects.check_email(request.POST)
    # print(is_email)
    if not is_email:
        messages.error(request, 'Email already in use.')
        return redirect('/')
    user_data = User.objects.create_user(request.POST)

    context = {
        'emails': User.objects.all()
    }
    return render(request, 'login_reg/success.html', context)
def login(request):

    return redirect('/success')

def success(request):
    return render(request, 'login_reg/success.html')
def logout(request):
    request.session.flush()
    return redirect('/')
