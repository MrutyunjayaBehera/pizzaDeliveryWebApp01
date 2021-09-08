from django.contrib import admin
from django.urls import path
from .views import acceptorder, declineorder, adminorders, userorders, addpizza, adminhomepageview, adminloginview, authenticateadmin, customerwelcomeview, deletepizza, homepageview, logoutadmin, placeorder, signupuser, userauthenticate, userloginview, userlogoutview


urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('adminauthenticate/', authenticateadmin),
    path('admin/homepage/', adminhomepageview, name='adminhomepage'),
    path('adminlogout/', logoutadmin),
    path('addpizza/', addpizza),
    path('deletepizza/<int:pizzapk>/', deletepizza),
    path('', homepageview, name='homepage'),
    path('signupuser/', signupuser),
    path('loginuser/', userloginview, name='userloginpage'),
    path('customer/welcome/', customerwelcomeview, name='customerpage'),
    path('customer/authenticate/', userauthenticate),
    path('userlogout/', userlogoutview),
    path('placeorder/', placeorder),
    path('userorders/', userorders),
    path('adminorders/', adminorders, name='adminorders'),
    path('acceptorder/<int:orderpk>/', acceptorder),
    path('declineorder/<int:orderpk>/', declineorder),
]










