from django import forms
from .models import user, vehicle

class FormUser(forms.ModelForm):
    class Meta:
        model = user
        exclude = () 
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXX.XXX.XXX-XX', 'pattern' : '[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', 'autocomplete':'off'}),
            'enrollment': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'})
        }

class FormVeh(forms.ModelForm):
    class Meta:
        model = vehicle
        exclude = () 
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'plate': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-select'})
        }