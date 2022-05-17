from distutils import extension
import email
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.forms import ValidationError
from rest_framework import serializers #importing restfrmaework
from.models import * # importing modeles we created
import datetime
from datetime import datetime as dt
import base64
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from .models import *


def username_validate(obj):
    user = User.objects.filter(username=obj)
    if user:
        
        raise ValidationError("Username already exists")

def email_validate(obj):
    user = User.objects.filter(email=obj)
    if user:
        raise ValidationError("Email already exists")

def mobile_validation(obj):
    if len(obj) > 12 or len(obj) < 10:
        raise ValidationError("Invalid mobile number")


class SerializerUser(serializers.ModelSerializer): 
    username = serializers.CharField(required=True,validators=[username_validate])
    email = serializers.EmailField(required=True,validators=[email_validate])

    class Meta:
        model = User
        fields =['id','email','username','password']


class BuyerSerializerUser(serializers.ModelSerializer): 
    username = serializers.CharField(required=True,validators=[username_validate])
    email = serializers.EmailField(required=True,validators=[email_validate])

    class Meta:
        model = User
        fields =['id','email','first_name','last_name','username','password']


#=====================================================#
#       USER REGISTRATION SERIALIZER END              #
#=====================================================#

class validateUser(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True )

class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        label=_("Username"),
        write_only=True,
        required=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True,
        required=True
    )
   

    def validate(self, attrs):
        print("ser")
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

    

#=====================================================#
#       USER PROFILE SERIALIZER START                 #
#=====================================================#