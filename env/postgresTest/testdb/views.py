from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from testdb.models import Product, Account, Student, Address, UploadImage
from django.db import models
import pdb
from django.shortcuts import render  
from testdb.forms import StudentForm  
from testdb.models import Customer
from testdb.forms import CustomerForm, AddressForm, UserImageForm
# Create your views here.
import pdb

def index(request):
    p = Product.objects.all()
    a = Account.objects.all()
    return render(request, "testdb/index.html", {'p':p, 'a':a})


def create(request, product_id, account_id):
    p1 = Product.objects.get(id=product_id)
    a1 = Account.objects.get(id=account_id)
    p1.accounts.add(a1)
    return render(request,"testdb/all.html", {'ans':p1.accounts.add(a1)})
    

def get_student(request):  
    student = StudentForm()  
    return render(request,"testdb/get_student.html",{'form':student})  


def create_student(request):
    if request.method == 'POST':
        # pdb.set_trace()
        # data = request.POST
        user = StudentForm(request.POST)
        if user.is_valid():
            # pdb.set_trace()
            s=Student(firstname=user.cleaned_data['firstname'], lastname=user.cleaned_data['lastname'], email= user.cleaned_data['email'])
            s.save()
        return HttpResponse(f"{s.firstname} and {s.email}")
    else:
        return HttpResponse(request, 'Invalid')
    

def one_student(request):
    customer = CustomerForm()
    return render(request, "testdb/one_student.html", {'form':customer})


def create_Customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerForm()
    return HttpResponse(f"{form.cleaned_data['name']}")


def get_address(request):
    address = AddressForm()
    return render(request,"testdb/get_address.html", {'form':address})

def register_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = AddressForm()
    return HttpResponse(f"{form.cleaned_data['street_no']} and {form.cleaned_data['area']} and {form.cleaned_data['city']}")


def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            img_object = form.instance
              
            return render(request, "testdb/image_form.html", {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImageForm()  
  
    return render(request, "testdb/image_form.html", {'form': form})  
