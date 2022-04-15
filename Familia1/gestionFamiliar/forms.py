from django import forms


class FamiliarForm(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    cumpleagnos = forms.DateField()
    email= forms.EmailField()
    edad= forms.IntegerField()
    