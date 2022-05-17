from django.urls import path

from .views import (
    productsview,
    productslistview,
    qr,
    qrurl,
    ProductStatusChnage
   
)

from. import buyer

urlpatterns = [
    # path('products/', DeliveryListView.as_view(), name='products'),
    # path('create-supplier/', create_supplier, name='create-supplier'),
    # path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
    path('products/', productsview, name='products'),
    path('productslist/', productslistview, name='products-list'),
    path('qr/', qr, name='qr'),

    path('qrapi/',qrurl.as_view(),name='qrapi'),

    path('product-status', ProductStatusChnage.as_view(), name='product-status'),


    path('buy/', buyer.BuyerProduct.as_view(), name='buy'),
    path('get-product', buyer.GetProductData.as_view(), name='get-product'),
]
