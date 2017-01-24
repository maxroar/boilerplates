from __future__ import unicode_literals
import re
from django.db import models
from django.contrib import messages

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserManager(models.Manager):
    REGEX_NAME = re.compile(r'^([a-zA-Z]){2,55}$')
    REGEX_EMAIL = re.compile(r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$')
    REGEX_PASS = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,20}$')

    def validate_reg(self, postData):
        valid_form = True
        if not REGEX_NAME.match(request.POST['first_name']):
        messages.add_message(request, messages.ERROR, 'First name must be only letters and at least 2 characters.')
        valid_form = False
        if not REGEX_NAME.match(request.POST['last_name']):
            messages.add_message(request, messages.ERROR, 'Last name must be only letters and at least 2 characters.')
            valid_form = False
        if not REGEX_EMAIL.match(request.POST['email']):
            messages.add_message(request, messages.ERROR, 'Please use a valid email.')
            valid_form = False
        if not REGEX_PASS.match(request.POST['pass1']):
            messages.add_message(request, messages.ERROR, 'Password must be at least 8 characters and contain at least 1 of each: capital letter, lowercase letter, number, special character.')
            valid_form = False
        if not request.POST['pass1'] == request.POST['pass2']:
            messages.add_message(request, messages.ERROR, 'Passwords must match.')
            valid_form = False
        return valid_form
    def validate_login(self, postData):
        
