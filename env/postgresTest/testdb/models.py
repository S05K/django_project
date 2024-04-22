from django import forms
from django.db import models
from django.forms import ModelForm
# Create your models here.
class Location(models.Model):
    name = name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    location = models.OneToOneField("Location", on_delete=models.CASCADE)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return self.location.name
    

class Account(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)


    def __str__(self):
        return self.name
    

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    accounts = models.ManyToManyField(Account)

    def __str__(self):
        return self.product_name
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Student(models.Model):
   firstname = models.CharField(max_length=50)  
   lastname  = models.CharField(max_length = 100)  
   email = models.CharField(max_length=50)
   def __str__(self):
       return self.firstname
   
    
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self):
        return self.book_name
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name
    

class Address(models.Model):
    street_no = models.IntegerField()
    area = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.city
    

class UploadImage(models.Model):  
    caption = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='images')  
  
    def __str__(self):  
        return self.caption  
