from __future__ import unicode_literals
import re
from django.db import models
import bcrypt
from django.contrib import messages

# Create your models here.
class UserManager(models.Manager):
    def validate_reg(self, postData):
        # regex patters
        REGEX_NAME = re.compile(r'^([a-zA-Z]){2,55}$')
        REGEX_EMAIL = re.compile(r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$')
        REGEX_PASS = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,20}$')
        # list to hold error messages
        errors = []
        if not REGEX_NAME.match(postData['first_name']):
            errors.append('First name must be only letters and at least 2 characters.')
        if not REGEX_NAME.match(postData['last_name']):
            errors.append('Last name must be only letters and at least 2 characters.')
        if not REGEX_EMAIL.match(postData['email']):
            errors.append('Please use a valid email.')
        if not REGEX_PASS.match(postData['pass1']):
            errors.append('Password must be at least 8 characters and contain at least 1 of each: capital letter, lowercase letter, number, special character.')
        if not postData['pass1'] == postData['pass2']:
            errors.append('Passwords must match.')
        return errors

    def check_email(self, postData):
        emails = User.objects.filter(email=postData['email'])
        print(emails[0].email)
        if emails:
            return False
        return True

    def create_user(self, postData):
        User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=bcrypt.hashpw(postData['pass1'].encode(), bcrypt.gensalt()))

    def login(self, postData):
        user_data = User.objects.filter(email=postData['email']).first()
        # print(user_obj)
        pwhash = user_data.password.encode()
        if pwhash == bcrypt.hashpw(postData['pass1'].encode(), pwhash):
            return True
        return False

    def set_session(self, postData):
        user_data = User.objects.filter(email=postData['email']).first()
        user_id = user_data.id
        return user_id

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    # def __getitem__(self, key):
    #     return self.user[key]
