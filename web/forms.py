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

class RegisterEmpleado(forms.Form):
    Nombre = forms.CharField()
    Direccion = forms.CharField()
    CodigoPostal = forms.CharField()
    RFCempleado = forms.CharField()
    Telefono = forms.CharField()
    emailEmpleado = forms.CharField()
    usernameEmpleado = forms.CharField()
    passwordEmpleado = forms.CharField(widget=forms.PasswordInput)    
        
        
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
    

class Registro_Trabajador(forms.Form):
    CodigoP = forms.CharField()
    RFC = forms.CharField()
    Direccion = forms.CharField()
    email = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) 