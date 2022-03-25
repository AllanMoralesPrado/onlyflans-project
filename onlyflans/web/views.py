from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Flan, ContactForm
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)

    sin_azucar = request.GET.get('no_sugar')
    sin_lactosa = request.GET.get('no_lactose')
    sin_huevos = request.GET.get('no_eggs')
    
    if sin_azucar == 'on':
        flanes_publicos = flanes_publicos.filter(no_sugar=True)
    
    if sin_lactosa == 'on':
        flanes_publicos = flanes_publicos.filter(no_lactose=True)

    if sin_huevos == 'on':
        flanes_publicos = flanes_publicos.filter(no_eggs=True)

    return render(request, 'index.html', {'flanes_publicos':flanes_publicos})

def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)

    sin_azucar = request.GET.get('no_sugar')
    sin_lactosa = request.GET.get('no_lactose')
    sin_huevos = request.GET.get('no_eggs')
    
    if sin_azucar == 'on':
        flanes_privados = flanes_privados.filter(no_sugar=True)
    
    if sin_lactosa == 'on':
        flanes_privados = flanes_privados.filter(no_lactose=True)

    if sin_huevos == 'on':
        flanes_privados = flanes_privados.filter(no_eggs=True)

    return render(request, 'welcome.html', {'flanes_privados':flanes_privados})

def exito(request):
    return render(request, 'success.html', {})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)            
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()

    return render(request, 'contactus.html', {'form':form})

