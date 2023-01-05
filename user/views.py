from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,reverse

#from .forms import RegisterForm,RegisterProfile

from django.contrib.auth.models import User 
from user.models import Profile
from user.forms import RegisterForm,ProfileForm, LoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from resumes.processor import get_profile
from datetime import datetime
import time
from django.core.mail import send_mail
from user.functions import message,subject,from_email
# Create your views here.




def register(request):    
    form = RegisterForm(request.POST or None) 
    if form.is_valid():
        username = form.cleaned_data.get("username") 
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        newUser = User(username = username,email=email,last_name=last_name,first_name=first_name) 
        newUser.set_password(password)
        newUser.save() 
        messages.info(request, "Başarıyla Kayıt oldunuz... Bu sayfada kişisel bilgilerinizi ekleyebilirsiniz.") 
        print(newUser)
        login(request,newUser)
        send_mail(subject=subject,message=message(first_name=first_name),from_email=from_email,recipient_list=[email])
        return redirect("profile")

    
    context = {      
        "form":form
    }
    return render(request,"register.html",context)


@login_required(login_url="login") 
def profile(request):
    print(request.user.username) 
    print(request.user.id)
    user = get_object_or_404(User, username = request.user.username)
    id = request.user.id
    if Profile.objects.filter(author_id = request.user.id).exists():
        profile = Profile.objects.get(author_id =id)
        form = ProfileForm(request.POST or None,instance=profile)  
        if form.is_valid():
            profile = form.save(commit=False)
            profile.author = request.user
            profile.save()
            messages.success(request,"Kişisel Bilgileriniz Başarıyla  Güncellendi...")
            return redirect("index")  
        return render(request,"user_update.html",{"form":form})
    else:
        print(user.username)
        newForm = ProfileForm(request.POST or None)
        if newForm.is_valid():
            profile = newForm.save(commit=False)
            profile.author = user
            profile.save()

            return redirect("index")
        return render(request,"profile.html",{"form":newForm})



@login_required(login_url="login")
def p_update(request):
    id = request.user.id 
    print(id)
    if Profile.objects.filter(author_id = id).exists():
        profile = Profile.objects.get(author_id =id)
        form = ProfileForm(request.POST or None,instance=profile)       
        if form.is_valid():
            profile = form.save(commit=False)
            profile.author = request.user
            profile.save()

            messages.success(request,"Kişisel Bilgileriniz Başarıyla  Güncellendi...")
            return redirect("index")      
        return render(request,"user_update.html",{"form":form})
 
    else:
        newForm = ProfileForm(request.POST or None)
        if newForm.is_valid():
            profile = newForm.save(commit=False)
            profile.author = request.user
            profile.save()
            messages.success(request,"Kişisel Bilgileriniz Başarıyla  Güncellendi...")
            return redirect("index")   
        return render(request,"user_update.html",{"form":newForm})
 

def Userlogin(request):
    form = LoginForm(request.POST or None) 
    context = {
        "form": form
    }
    
    if form.is_valid(): 
        username = form.cleaned_data.get("username") 
        password = form.cleaned_data.get("password")        
        user = authenticate(username = username,password=password) 
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı") 
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız...")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)


@login_required(login_url="login")
def Userlogout(request): 
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız... ")
    return redirect("index")
    