from django.shortcuts import render,HttpResponse,redirect
from resumes.forms import ResumeForm
from resumes.models import Resume
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
import requests
from django.core.mail import send_mail
from resumes.mail_text import message,subject,from_email 
# Create your views here.

def index(request): 
    context = {"numbers":[1,2,3,4,5,6,], "number1":10, "number2":20}
    return render(request,"index.html", context)

@login_required(login_url="login")
def mycv(request):
    id = request.user.id
    if Resume.objects.filter(author_id = id):
        resume = Resume.objects.get(author_id=id)
        form = ResumeForm(request.POST or None,request.FILES or None,instance=resume)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.author = request.user
            cv.save()
            messages.success(request,"Özgeçmişiniz Başarıyla Güncellendi...")
            return redirect ("index")
        return render(request,"cv_update.html",{"form":form})
    else:
        newform = ResumeForm(request.POST or None,request.FILES or None)
        if newform.is_valid():
            cv = newform.save(commit=False)
            cv.author = request.user
            cv.save()
            messages.success(request,"CV Başarıyla Oluşturuldu...")
            return redirect("index")
        return render(request,"addcv.html",{"form":newform})

@login_required(login_url="login")
def detail(request,id):
    resume = Resume.objects.get(id=id)
    if request.user==resume.author: 
        messages.success(request,"Özgeçmişiniz...")
        print(request.user)
        print(resume.author.email)
        print(id)
        return render(request,"detail.html",{"resume":resume})
    else:
        resume = Resume.objects.get(id=id)
        send_mail(subject=subject,message=message(resume.author.first_name),from_email=from_email,recipient_list=[resume.author.email])
        return render(request,"detail.html",{"resume":resume})
  
def cvss(request):
    keyword = request.GET.get("keyword")
    if keyword:
        resumes = Resume.objects.filter(position__contains=keyword)
        return render(request,"cvss.html",{"resumes":resumes})
    resumes = Resume.objects.all() 
    return render(request,"cvss.html",{"resumes":resumes})

@login_required(login_url="login")
def deleteCv(request):
    id = request.user.id
    resume = Resume.objects.get(author_id = id)
    resume.delete()
    messages.success(request,"Özgeçmişiniz Başarıyla Silindi...")
    return redirect("index")

base_url = "https://api.github.com/users/"  
def github(request):
    if request.method == "POST":
        githubname = request.POST.get("githubname")
        print("test")
        response = requests.get(base_url + githubname) 
        response_repos = requests.get(base_url + githubname + "/repos")
        print(response)
        user_info = response.json()
        repos = response_repos.json()
        print(user_info)
        context = {"error":"Kullanıcı Bulunamadı..."}
        if "message" in user_info:  
            print("test")
            return render(request,"github.html",context)   
        else:
            return render(request,"github.html",{"profile":user_info,"repos":repos})
    else:
        return render(request,"github.html")
