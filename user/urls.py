
from django.urls import path
from .import views
from .views import logout_page, login_page, govlogout_page
urlpatterns = [
    path('',views.SelectionLogin.as_view(),name='select-login'),
    path('govlogin',views.GovLogin.as_view(),name='gov-login'),
    path('login',views.UserLogin.as_view(),name='login'),
    path('register',views.RegisterUser.as_view(),name='register'),
    path('dashboard',views.Dashboard.as_view(),name='dashboard'),
    path('gov_dashboard', views.GovDashboard, name='gov-dashboard'),
    path('store-dashboard', views.BuyerDashboard.as_view(), name='store_dashboard'),
    path('govlogout/', govlogout_page, name='gov-logout'),
    path('logout/', logout_page, name='logout'),
    path('store-login', views.BuyerLogin.as_view(), name='store-login'),
    path('store-register', views.RegisterBuyer.as_view(), name='store-register'),

    

]