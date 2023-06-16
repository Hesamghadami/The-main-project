from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

def home(req):
    if req.method == 'GET':
        return render(req, 'home/index.html')
    elif req.method == 'POST':
        form = NewsLetterForm(req.POST)
        if form.is_valid():
            form.save()   
        return redirect('/')
    

def contact(req):
    if req.method == 'GET':
        return render(req, 'home/contact.html')
    
    elif req.method == 'POST':
        form_contact = ContactUsForm(req.POST)
        if form_contact.is_valid():
            form_contact.save()
        return redirect('/')
    
    
    


# Create your views here.
