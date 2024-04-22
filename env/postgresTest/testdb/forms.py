from django import forms  
from testdb.models import Customer, Address, UploadImage
from django.forms import ModelForm


class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)  
    email = forms.CharField(label="Enter your email", max_length=50)



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "number"]


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ["street_no", "area", "city"]


class UserImageForm(ModelForm):  
    class Meta:  
        model = UploadImage   
        fields = ["caption", "image"]
