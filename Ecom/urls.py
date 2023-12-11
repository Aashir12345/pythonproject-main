from django.urls import path
from . import views
from Ecom.controller import  authview,cart

urlpatterns= [

    path('',views.home , name="home"),
    path('productviwes/<str:myslug>',views.productviwes , name="productviwes"),
    path('productDetails/<str:cat_slug>/<str:prod_slug>', views.productDetails , name="productDetails"),




    path('register',authview.register , name="register"),
    path('login',authview.loginpage, name="login"),

    path('addtocart',cart.addtocart,name="addtocart")

    
]