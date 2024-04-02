from django import forms
from .models import Pedidos
from django.contrib.auth.forms import UserCreationForm


class Register(forms.Form):
    RazonS = forms.CharField()
    DireccionF = forms.CharField()
    CodigoP = forms.CharField()
    RFC = forms.CharField()
    DireccionE = forms.CharField()
    email = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    clienteCheckbox = forms.BooleanField(required=False)
    proveedorCheckbox = forms.BooleanField(required=False)

   
        
        
class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo Electrónico', max_length=255, required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=True)

 


class Pedido(forms.Form):
    Moneda = forms.CharField()
    Solicitante = forms.CharField()
    Empresa = forms.CharField()
    Direccion = forms.CharField()
    Telefono = forms.CharField()
    Cantidad = forms.CharField()
    Detalles = forms.CharField()
    

