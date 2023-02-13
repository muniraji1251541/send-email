from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request,'home.html')

def register(request):
    uf=Userform()
    pf=Profileform()
    d={'uf':uf,'pf':pf}
    if request.method=='POST' and request.FILES:
        ufd=Userform(request.POST)
        pfd=Profileform(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            ufo=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            ufo.set_password(password)
            ufo.save()

            pfo=pfd.save(commit=False)
            pfo.profile_user=ufo
            pfo.save()

            send_mail('Registration','Registration is successfully','muniraji775@gmail.com',[ufo.email],fail_silently=False)

            return HttpResponse('User data is register successfully')

    return render(request,'register.html',d)