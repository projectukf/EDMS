from django import forms

# from .models import Bill, Products, Season, Drop, Product, Order, Delivery
from .models import Products

# class SupplierForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'name',
#         'data-val': 'true',
#         'data-val-required': 'Please enter name',
#     }))
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'address',
#         'data-val': 'true',
#         'data-val-required': 'Please enter address',
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'id': 'email',
#         'data-val': 'true',
#         'data-val-required': 'Please enter email',
#     }))
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'username',
#         'data-val': 'true',
#         'data-val-required': 'Please enter username',
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter password',
#     }))
#     retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'retype_password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter retype_password',
#     }))


# class BuyerForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'name',
#         'data-val': 'true',
#         'data-val-required': 'Please enter name',
#     }))
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'address',
#         'data-val': 'true',
#         'data-val-required': 'Please enter address',
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'id': 'email',
#         'data-val': 'true',
#         'data-val-required': 'Please enter email',
#     }))
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'username',
#         'data-val': 'true',
#         'data-val-required': 'Please enter username',
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter password',
#     }))
#     retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'retype_password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter retype_password',
#     }))


# class SeasonForm(forms.ModelForm):
#     class Meta:
#         model = Season
#         fields = ['name', 'description']

#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'name'
#             }),
#             'description': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'description'
#             })
#         }


# class DropForm(forms.ModelForm):
#     class Meta:
#         model = Drop
#         fields = ['name']
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'name'
#             })
#         }

# class BillForm(forms.ModelForm):
#     class Meta:
#         model = Bill
#         fields = ['name']
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'name'
#             })
#         }

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Products
#         fields = ['name', 'qty', 'price']
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'name'
#             }),
#             'qty': forms.NumberInput(attrs={
#                 'class': 'form-control', 'id': 'qty'
#             }),
#             'price': forms.NumberInput(attrs={
#                 'class': 'form-control', 'id': 'price'
#             })
#         }


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = [
#             'supplier', 'product', 'design', 'color', 'buyer', 'season', 'drop'
#         ]

#         widgets = {
#             'supplier': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'supplier'
#             }),
#             'product': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'product'
#             }),
#             'design': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'design'
#             }),
#             'color': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'color'
#             }),
#             'buyer': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'buyer'
#             }),
#             'season': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'season'
#             }),
#             'drop': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'drop'
#             }),
#         }


# class DeliveryForm(forms.ModelForm):
#     class Meta:
#         model = Delivery
#         fields = '__all__'

#         widgets = {
#             'order': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'order'
#             }),
#             'courier_name': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'courier_name'
#             }),
#         }


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Products
#         fields = ['name', 'product_id', 'qty', 'price']
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'name'
#             }),
#             'qty': forms.NumberInput(attrs={
#                 'class': 'form-control', 'id': 'qty'
#             }),
#             'price': forms.NumberInput(attrs={
#                 'class': 'form-control', 'id': 'price'
#             })
#         }