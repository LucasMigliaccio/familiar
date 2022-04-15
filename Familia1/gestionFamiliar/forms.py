from django import forms


class FamiliarForm(forms.ModelForm):
    
    Nombre = forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)
    Cumpleagnos = forms.DateField()
    Email= forms.EmailField()
    Edad= forms.IntegerField()
    