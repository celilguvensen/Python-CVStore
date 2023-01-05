from user.models import Profile
from resumes.models import Resume
from django.shortcuts import render
import time
from datetime import datetime,date
import locale


def get_profile(request):
    now = datetime.now()
    locale.setlocale(locale.LC_ALL,"") 
    current_now = now.strftime("%d/%m/%Y")
    current_now = current_now.replace("/",".")
    day =datetime.strftime(now,"%A")
    liste = list()
    profile_l = set()
    resumes = Resume.objects.all() 
    if resumes:          
        for resume in resumes: 
            if resume.author_id in liste:
                pass
            else: 
                liste.append(resume.author_id)  
        for id in liste:
            if Profile.objects.filter(author_id = id).exists():
                profile = Profile.objects.get(author_id = id)                     
                profile_l.add(profile)
            else:
                newprofile = Profile.objects.create(author_id = id)
                Profile.objects.filter(author_id = id).update(city = "Mevcut Değil",phone="Mevcut Değil")
                profile_l.add(newprofile)
        return {"profiles":profile_l,"current":current_now,"day":day}
    else:
        return {}