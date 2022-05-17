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

# Create your views here.
@login_required(login_url='gov-login')
def qr(request):
   if request.method=="POST":
      data = request.POST

      product_id = data.get("product_id")
      exp_date = data.get("exp_date")
      qty = int(data.get("qty"))
      qr_code=QrCode.objects.filter(org_id=str(request.user),product_id=product_id,created_date=date.today()).first()
      if qr_code is None:
        print(qr_code)
        for x in range(qty):
            while True:
                qr_id = random.randint(0,9999999999)
                qr_code=QrCode.objects.filter(qr_id=str(qr_id)).first()
                if qr_code is None:
                    break
            
            d = date.today() + timedelta(days=int(exp_date))
            QrCode.objects.create(qr_id=str(qr_id),org_id=str(request.user),product_id=product_id,exp_date=d)
   qr_code=QrCode.objects.filter(org_id=str(request.user),product_id=product_id)
   return render(request,"qr.html",{'qr_code':qr_code})

@login_required(login_url='gov-login')
def productsview(request):
    if request.method == "POST":
        data = request.POST
        
        product_price = int(data.get("price"))
        total_price  = int(product_price)*int(data.get("qty"))
        # print(total_price)
        org_id = Organisation.objects.filter(user=request.user).first()
        # print(org_id)
        # print(request.user)
        if org_id:
            Pro_obj = Products.objects.create(
                name = data.get("name"),
                product_id = data.get("product_id"),
                org_id = org_id,
                qty = data.get("qty"),
                status = PENDING_STATE,
                exp_time = data.get("exp_time"),
                price = total_price,
                single_price = product_price
            )
            Pro_obj.save()
            
            products = Products.objects.filter(org_id = org_id)
            context = {
            'products': products
            }
            return render(request, 'gov/product_list.html', context)
        # return redirect('some-view-name', context)
    return render(request, 'gov/create_product.html')






@login_required(login_url='gov-login')
def productslistview(request):
    user = request.user
    if user.is_superuser:
        products = Products.objects.filter(status=PENDING_STATE)
    else:
        org_id = Organisation.objects.filter(user=request.user).first()
        products = Products.objects.filter(org_id = org_id)
    context = {
    'products': products,'user':user.is_superuser
    }
    print(context)
    return render(request, 'gov/product_list.html', context)


class qrurl(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = {
            'task': 123, 
        }
        return Response(data, status=status.HTTP_200_OK)


class ProductStatusChnage(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        
        data = request.data
        if data:
            status_data = data["status"]
            product_id = data["product_id"]
            Products.objects.filter(id=product_id).update(status=status_data)
        return Response(data={"detail":"Successfully Updated","status":"true"}, status=status.HTTP_200_OK)

