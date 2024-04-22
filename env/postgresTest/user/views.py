from base64 import urlsafe_b64decode
from base64 import *
import base64
import datetime
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
import token
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db import models
from django.contrib.auth.models import User, auth
from user.forms import UserForm
from .forms import UserLoginForm
from user.models import CustomUser, JobApplication
from django.core.mail import send_mail
import pdb
from user.models import Job
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# Create your views here.

def index(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            cleaned_data = user_form.cleaned_data
            user = CustomUser(
                first_name=cleaned_data['first_name'],
                username=cleaned_data['username'],
                email=cleaned_data['email'],
                image=cleaned_data['image']
            )
            user.set_password(cleaned_data['password'])
            user.save()
            # subject = "Testing maill"
            # message = f"Welcome!!! {user.username}"
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [user.email,]
            # send_mail(subject,message,email_from,recipient_list)
            return HttpResponse(f"{user.email} and {user.password}")
    else:
        user_form = UserForm()
    return render(request, 'user/index.html', {'form': user_form})
    

def login(request):
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("user:home"))
            else:
                return HttpResponse("Invalid username or password")
        else:
            print("Form Errors:", user_form.errors)  
            return HttpResponse("Form data is not valid. Errors: {}".format(user_form.errors))

    else:
        log = UserLoginForm()
        return render(request, 'user/login.html', {'form': log})


def home(request):
    return render(request, 'user/home.html')


def jobs(request):
    all_jobs = Job.objects.all()
    return render(request,"user/jobs.html", {'jobs':all_jobs})


# To find current user.........
def get_user(request):
     user = request.user
     email = user.email 
     username = user.username
     return HttpResponse(f"{user}, {email}, {username} ")


def forgot_password(request):
    return render(request, "user/forgot_password.html")

def find_email(request):
    # pdb.set_trace()
    if request.method == 'POST':
        user_email = request.POST.get('email')
        if CustomUser.objects.filter(email=user_email).exists():
            user = CustomUser.objects.get(email=user_email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            subject = "Password reset email"
            # a = request.build_absolute_uri(reverse('user:reset_password', kwargs={'uidb64': uid, 'token': token}))
            a = f"http://127.0.0.1:8000/user/reset_password/{uid}/{token}/"
            message = f"Click <a href={a}>here</a> to reset your password."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user_email,]
            send_mail(subject,message,email_from,recipient_list)
            return HttpResponse(f"{user_email}, we have sent you mail")
        else:
            return HttpResponse("<h1> not present </h1>")

            
        
        

def reset_password(request, uidb64, token):
    return render(request,"user/reset_password.html", {'uidb64':uidb64, 'token':token})

def update_password(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = CustomUser.objects.get(pk=uid)
    new_password =  request.POST.get('password')
    user.set_password(new_password)
    user.save()
    return HttpResponseRedirect(reverse("user:login"))
   
        



@login_required
def apply_for_job(request, user_id, job_id):
    user = request.user 
    job = Job.objects.get(pk=job_id)
    if JobApplication.objects.filter(user=user, job=job).exists():
        return HttpResponse(f"{user.username} you are already applied for this job")
    else:
        application = JobApplication.objects.create(user=user, job=job)
        return HttpResponse(f"{application}") 


def search_jobs(request):
    user_jobs = request.POST.get('job')
    ans = str(user_jobs)
    jobs = Job.objects.filter(title = ans.capitalize())
    return render(request, "user/filtered_jobs.html", {'jobs':jobs})