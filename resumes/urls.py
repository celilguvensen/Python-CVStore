from django.urls import path
from . import views


 
 
urlpatterns = [

    
    path("mycv/",views.mycv,name="mycv"),
    path("resumes/",views.cvss,name="cvss"),
    path("detail/<int:id>",views.detail,name="detail"),
    path("delete/",views.deleteCv,name="delete"),


]