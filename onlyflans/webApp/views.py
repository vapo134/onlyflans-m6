from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Flan, ContactForm
from .forms import ContactFormForm

# Create your views here.
def index(request):
    #flan = Flan.objects.all()
    flan = Flan.objects.filter(is_private = False)
    return render(request,'index.html',{'flan':flan})

def about (request):
    return render(request, 'about.html',{})

@login_required
def welcome (request):
    flan = Flan.objects.filter(is_private = True)
    return render(request, 'welcome.html',{'flan':flan})

def contacto(request):
    if request.method=='POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contacto_form = ContactForm.objects.create(**form.cleaned_data)
            messages.success(request, 'Mensaje enviado correctamente')
            return redirect('exito')
    else:
        form = ContactFormForm()
    
    return render(request,'contacto.html',{'form':form})

def exito (request):
    return render(request,'exito.html',{})