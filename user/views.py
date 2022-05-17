from msilib.schema import Class
from django.shortcuts import render,redirect
from rest_framework.views import APIView# normal view can written API data
from rest_framework.response import Response# get a perticular response every thing is okey then give 200 response
from rest_framework import status # basically sent back status
from django.contrib import messages
from django.contrib.auth.models import User
from .serializers import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as lg, logout,login
from rest_framework.exceptions import (
 APIException,               #for api exception
 ValidationError
)
import datetime
import base64
import os
from .models import *
import requests
from .forms import LoginForm
# from store.models import Product, Supplier, Buyer, Order
def logout_page(request):
    logout(request)
    return redirect('login')

def govlogout_page(request):
    logout(request)
    return redirect('gov-login')





def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)

#Selection page rendering==========================
class SelectionLogin(APIView):
    def get(self,request):
        # print("ok")
        return Response({"detail":"success"},status=status.HTTP_200_OK,template_name='login_selection.html')
#================================================

class GovLogin(APIView):
    def get(self,request):
        # print("ok")
        return Response({"detail":"success","user":"govt"},status=status.HTTP_200_OK,template_name='govlogin.html')

    def post(self,request):
        
        ser = validateUser(data=request.data)
        if ser.is_valid():


            user = User.objects.filter(username=request.POST["username"]).first()
            # print("user",user)
            if user:
                serializer = AuthTokenSerializer(data=request.data)
                
                if serializer.is_valid():
                    user = serializer.validated_data['user']
                    
                    # if user.last_login:
                    if user.is_superuser:
                        lg(request, user)
                        return redirect("gov-dashboard")
                    else:
                        return redirect("gov-login")
                    # else:
                    #     lg(request, user)
                        
                    #     return redirect("profile")
                else:
                    
                    error_list = [serializer.errors[error][0] for error in serializer.errors]
                    err = error_list[0].split("string='")
                    # print("error",err)
                    return Response({"messages":"error","detail":err[0]},status=status.HTTP_400_BAD_REQUEST,template_name='govlogin.html')
            else:
                # print("error")
                return Response({"messages":"error","detail":"User not exists"},status=status.HTTP_400_BAD_REQUEST,template_name='govlogin.html')


        else:
            error_list = [ser.errors[error][0] for error in ser.errors]
            err = error_list[0].split("string='")
            print("error",err)
            return Response({"messages":"error","detail":err[0]},status=status.HTTP_400_BAD_REQUEST,template_name='govlogin.html')


class UserLogin(APIView):
    def get(self,request):
        # print("ok")
        return Response({"detail":"success"},status=status.HTTP_200_OK,template_name='login.html')

    def post(self,request):
        ser = validateUser(data=request.data)
        if ser.is_valid():


            user = User.objects.filter(username=request.POST["username"]).first()
            print("user",user)
            if user:
                serializer = AuthTokenSerializer(data=request.data)
                
                if serializer.is_valid():
                    user = serializer.validated_data['user']
                    
                    # if user.last_login:
                    lg(request, user)
                    return redirect("dashboard")
                    # else:
                    #     lg(request, user)
                        
                    #     return redirect("profile")
                else:
                    
                    error_list = [serializer.errors[error][0] for error in serializer.errors]
                    err = error_list[0].split("string='")
                    print("error",err)
                    return Response({"messages":"error","detail":err[0]},status=status.HTTP_400_BAD_REQUEST,template_name='login.html')
            else:
                print("error")
                return Response({"messages":"error","detail":"User not exists"},status=status.HTTP_400_BAD_REQUEST,template_name='login.html')


        else:
            error_list = [ser.errors[error][0] for error in ser.errors]
            err = error_list[0].split("string='")
            print("error",err)
            return Response({"messages":"error","detail":err[0]},status=status.HTTP_400_BAD_REQUEST,template_name='login.html')


class BuyerLogin(APIView):
    def get(self,request):
        # print("ok")
        return Response({"detail":"success"},status=status.HTTP_200_OK,template_name='buyer_login.html')

    def post(self,request):
        ser = validateUser(data=request.data)
        if ser.is_valid():


            user = User.objects.filter(username=request.POST["username"]).first()
            print("user",user)
            if user:
                serializer = AuthTokenSerializer(data=request.data)
                
                if serializer.is_valid():
                    user = serializer.validated_data['user']
                    
                    # if user.last_login:
                    lg(request, user)
                    return redirect("store_dashboard")
                   
                else:
                    
                    error_list = [serializer.errors[error][0] for error in serializer.errors]
                    err = error_list[0].split("string='")
                    print("error",err)
                    return Response({"messages":"error","detail":err[0]},status=status.HTTP_400_BAD_REQUEST,template_name='buyer_login.html')
            else:
                print("error")
                return Response({"messages":"error","detail":"User not exists"},status=status.HTTP_400_BAD_REQUEST,template_name='buyer_login.html')


        else:
            error_list = [ser.errors[error][0] for error in ser.errors]
            err = error_list[0].split("string='")
            print("error",err)
            return Response({"messages":"error","detail":err[0]},status=status.HTTP_400_BAD_REQUEST,template_name='buyer_login.html')





class RegisterUser(APIView):
    def get(self,request):
        
        return Response({"detail":"success"},status=status.HTTP_200_OK,template_name='register.html')

    def post(self,request):
        # print("set",request.data)
        userserializer = SerializerUser(data=request.data)
        # print("1212")
        if userserializer.is_valid():
            # print("ok")
            # print(request.data['org_name'])
            new_user = userserializer.save(password=make_password(userserializer.validated_data['password']))
            org_obj = Organisation.objects.create(user=new_user,org_name=request.data['org_name'])
        else:
           
            error_list = [userserializer.errors[error][0] for error in userserializer.errors]
            err = error_list[0].split("string='")
            return Response({"messages":"error","detail":err[0]},status=status.HTTP_400_BAD_REQUEST,template_name='register.html')

        return redirect('login')
        # return Response({"detail":"success"},status=status.HTTP_200_OK,template_name='register.html')

class RegisterBuyer(APIView):
    def get(self,request):
        
        return Response({"detail":"success"},status=status.HTTP_200_OK,template_name='buyer_reg.html')

    def post(self,request):
      
        userserializer = BuyerSerializerUser(data=request.data)
       
        if userserializer.is_valid():
           
            new_user = userserializer.save(password=make_password(userserializer.validated_data['password']))
            buyer_obj = StoreBuyer.objects.create(user=new_user,store_name=request.data['store_name'])
        else:
           
            error_list = [userserializer.errors[error][0] for error in userserializer.errors]
            err = error_list[0].split("string='")
            return Response({"messages":"error","detail":err[0]},status=status.HTTP_400_BAD_REQUEST,template_name='buyer_reg.html')

        return redirect('store-login')
        # return Response({"detail":"success"},status=status.HTTP_200_OK,template_name='register.html')


class Dashboard(APIView):
    def get(self,request):
        user= request.user
        print("p456")

        return Response({"detail":"success"},status=status.HTTP_200_OK,template_name='dashboard.html') 

class BuyerDashboard(APIView):
    def get(self,request):
        user= request.user
        
        print("ploklpl")
        return Response({"detail":"success"},status=status.HTTP_200_OK,template_name='buyer_dashboard.html') 


@login_required(login_url='gov-login')
def GovDashboard(request):
    return render(request, 'gov_dashboard.html')