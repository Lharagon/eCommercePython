# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import re
# import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration(self,name,user_name,email,password,confirm_password):
        if (len(name)>=3):

            if (user_name and len(user_name)>=3 and user_name.isalpha()):
                if ( email and EMAIL_REGEX.match(email)):
                    if (password and len(password) >=5 and password == confirm_password):
                        mypassword = password.encode()
                        hashed = bcrypt.hashpw(mypassword,bcrypt.gensalt())
                        list =[hashed]
                        return list
        else:
            return None
    def login(self,userPassword,password):
        dabasePassword = userPassword.encode()
        print dabasePassword
        mypassword = password.encode()
        print mypassword
        print bcrypt.hashpw(mypassword,dabasePassword)
        if(bcrypt.hashpw(mypassword,dabasePassword)==dabasePassword):

            return True
        else:

            return False




class User(models.Model):
    name = models.CharField(max_length=45)
    user_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45, default='none')
    password = models.CharField(max_length=100)
    date_hired = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()



class Watch(models.Model):
    name = models.CharField(max_length=250)
    details = models.CharField(max_length=1000)
    price = models.CharField(max_length=10)
    user = models.ForeignKey('User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)