from django.db import models

from user.models import User

import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
from user import models as user_model
# Create your models here.
import random
class QrCode(models.Model):
   qr_id=models.CharField(max_length=120, unique=True)
   org_id = models.CharField(max_length=200)
   product_id = models.CharField(max_length=200,null=True)
   exp_date = models.DateField()
   created_date = models.DateField(auto_now_add=True)
   image=models.ImageField(upload_to='qrcode',blank=True)

   def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.qr_id)
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'qr{self.qr_id}{random.randint(0,9999)}.png',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)

# class Supplier(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=120, unique=True)
#     address = models.CharField(max_length=220)
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Buyer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=120, unique=True)
#     address = models.CharField(max_length=220)
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Season(models.Model):
#     name = models.CharField(max_length=120, unique=True)
#     description = models.CharField(max_length=220)
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Drop(models.Model):
#     name = models.CharField(max_length=120, unique=True)
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=120, unique=True)
#     sortno = models.PositiveIntegerField()
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Order(models.Model):
#     STATUS_CHOICE = (
#         ('pending', 'Pending'),
#         ('decline', 'Decline'),
#         ('approved', 'Approved'),
#         ('processing', 'Processing'),
#         ('complete', 'Complete'),
#         ('bulk', 'Bulk'),
#     )
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     design = models.CharField(max_length=50)
#     color = models.CharField(max_length=50)
#     buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
#     season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
#     drop = models.ForeignKey(Drop, on_delete=models.CASCADE, null=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICE)
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.product.name


# class Delivery(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     courier_name = models.CharField(max_length=120)
#     created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.courier_name

# # ##################################################################################

# class Products(models.Model):
#     name = models.CharField(max_length=120)
#     qty = models.IntegerField()
#     price = models.IntegerField()
#     created_date = models.DateField(auto_now_add=True)

# class Bill(models.Model):
#     name = models.CharField(max_length=120)
#     total = models.IntegerField(default=0)
#     created_date = models.DateField(auto_now_add=True)

# class BillItems(models.Model):
#     bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
#     name = models.CharField(max_length=120)
#     qty = models.IntegerField()
#     price = models.IntegerField()

class Products(models.Model):
    name = models.CharField(max_length=120,unique=True)
    product_id = models.CharField(max_length=120,null=True)
    org_id =  models.ForeignKey(user_model.Organisation, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField()
    exp_time = models.IntegerField()
    status = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    single_price = models.IntegerField()