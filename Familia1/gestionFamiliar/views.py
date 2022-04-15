
from django.shortcuts import render
from .forms import FamiliarForm
from .models import Familiar
from django.http import HttpResponse
# Create your views here.

def base (request):
    return render(request,"base.html")

def familyForm(request):
    if request.method == "POST":
        myform= FamiliarForm(request.POST)
        if myform.is_valid:
            print(myform)
            familyinfo= myform.cleaned_data
            familia= Familiar(nombre= familyinfo["Nombre"],apellido=familyinfo["Apellido"],cumpleagnos=familyinfo["Cumpleagnos"],email=familyinfo["Email"],edad=familyinfo["Edad"])
            familia.save()
            return HttpResponse(f"Familiar registrado" )
    else:
        myform=FamiliarForm()
    return render(request,"familiarform.html",{"myform":myform})
