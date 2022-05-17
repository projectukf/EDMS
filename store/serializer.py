from distutils import extension
import email
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.forms import ValidationError
from rest_framework import serializers

from user.models import Organisation #importing restfrmaework
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


class OrganizationUserSrializer(serializers.ModelSerializer): 
   

    class Meta:
        model = Organisation
        fields =['id','user','org_name']


class ProductSrializer(serializers.ModelSerializer): 
   

    class Meta:
        model = Products
        fields =['id','name','product_id','org_id','qty','single_price']


class QrCodeSrializer(serializers.ModelSerializer): 
   

    class Meta:
        model = QrCode
        fields =['id','product_id','qr_id']
