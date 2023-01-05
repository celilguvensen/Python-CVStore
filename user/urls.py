from django.urls import path
from . import views


 

urlpatterns = [ 
    path("register/",views.register,name="register"),
    path("profile/",views.profile,name="profile"), 
    path("update/",views.p_update,name="update"),
    path("login/",views.Userlogin,name="login"),
    path("logout/",views.Userlogout,name="logout"),

]