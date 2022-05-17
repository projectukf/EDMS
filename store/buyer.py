from itertools import product
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.viewsets import *
from rest_framework.views import APIView
from rest_framework import status, generics
from user.models import Organisation, User
from rest_framework import permissions

from .models import Products, QrCode

from datetime import datetime, date  
from datetime import timedelta 
import random
from .constant import *
from . serializer import *




class BuyerProduct(APIView):
    def get(self,request):

        org_list = Organisation.objects.all()
        serializer_data = OrganizationUserSrializer(org_list,many=True)
        # print(serializer_data.data)
        context = serializer_data.data
        return Response({"detail":"success","org_data":context},status=status.HTTP_200_OK,template_name='store/buy_product.html') 
        
    def post(self,request):
       
            data = request.POST
            
            # product_price = int(data.get("price"))
            # total_price  = int(product_price)*int(data.get("qty"))
            # # print(total_price)
            
            # Pro_obj = Products.objects.create(
            #     name = data.get("name"),
            #     product_id = data.get("product_id"),
            #     org_id = str(request.user),
            #     qty = data.get("qty"),
            #     status = PENDING_STATE,
            #     exp_time = data.get("exp_time"),
            #     price = total_price
            # )
            # Pro_obj.save()
            
            products = Products.objects.filter(org_id = request.user)
            context = {
            'products': products
            }
            return render(request, 'store/buy_product.html', context)
            # return redirect('some-view-name', context)
            # return render(request, 'store/buy_product.html')  


class GetProductData(APIView):
    def post(self,request):
        jsondata = request.data
        product_obj = Products.objects.filter(org_id=jsondata['org_id'],status=APPROVED_STATE)
        serializer_data = ProductSrializer(product_obj,many=True)
        
        qr_data = QrCode.objects.filter(org_id__in=list(product_obj.values_list('org_id__user__username',flat=True)))
        qr_serializer = QrCodeSrializer(qr_data,many=True)
        
        return Response({"detail":"success","product_data":serializer_data.data,"qr_data":qr_serializer.data},status=status.HTTP_200_OK,template_name='store/buy_product.html')
