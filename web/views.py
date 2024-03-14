from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login , authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import Register ,LoginForm, Pedido, RegisterEmpleado
from .models import Usuario, Pedidos
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from smtplib import SMTPServerDisconnected



def inicio(request):
    
    context={}
    return render(request, "inicio.html", context)

def send_email(email):
    print(email )


#Esta funcion sirve para registrar un usuario en la base de datos
def registro(request):
    if request.method == 'POST':
        # email = request.POST.get('email')
        # send_email(email)
        form = Register(request.POST)

        if form.is_valid():
            # Obtén los datos del formulario
            RazonS = form.cleaned_data['RazonS']
            DireccionF = form.cleaned_data['DireccionF']
            CodigoP = form.cleaned_data['CodigoP']
            RFC = form.cleaned_data['RFC']
            DireccionE = form.cleaned_data['DireccionE']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Usa make_password para hashear la contraseña antes de almacenarla
            hashed_password = make_password(password)

            # Crea una instancia de Usuario y guárdala en la base de datos
            usuario = Usuario(RazonS=RazonS, DireccionF=DireccionF, CodigoP=CodigoP, RFC=RFC, DireccionE=DireccionE, email=email, username=username, password=hashed_password)
            usuario.save()

            # # Envía el correo de confirmación
            # subject = 'Confirmación de registro'
            # message = f'Tu cuenta en la plataforma ha sido creada con éxito.'
            # from_email = settings.DEFAULT_FROM_EMAIL
            # recipient_list = [email]
            

            # try:

            #     send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            # except SMTPServerDisconnected as e:
            #    print(f"SMTPServerDisconnected: {e}")
            

            

            

            # Redirecciona a una página de éxito o realiza otras acciones necesarias
            return redirect('web:login')  # Cambia 'pagina_de_exito' por la URL a la que quieras redirigir

    else:
        form = Register()
        
    context = {
        'form': form,
    }
    return render(request, "registro.html", context)


#Esta funcion sirve para que el usuario inicie sesion autenticandolo y verificandolo desde la base de datos
def login(request):
    if request.user.is_authenticated:
        return redirect('web:dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = Usuario.objects.get(email=email)
                if check_password(password, user.password):
                    auth_login(request, user)  # Iniciar sesión manualmente
                    print(f'Usuario autenticado manualmente: {user}')
                    return redirect('web:dashboard')  # Redirigir a la página después de la autenticación
                else:
                    print('Contraseña incorrecta')
            except Usuario.DoesNotExist:
                print('Usuario no encontrado')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'registration/login.html', context)




#Esta funcion sirve para desloguear al usuario de su cuenta y mandarlo al login
def logout(request):
    auth_logout(request)

    return redirect('web:login')


#Esta funcion sirve para guardar la orden de trabajo generada por el usuario logueado en el dashboard
@login_required
def dashboard(request):
    if request.method == 'POST':
        form = Pedido(request.POST)
        if form.is_valid():
            Moneda = form.cleaned_data['Moneda']
            Solicitante = form.cleaned_data['Solicitante']
            Empresa = form.cleaned_data['Empresa']
            Direccion = form.cleaned_data['Direccion']
            Telefono = form.cleaned_data['Telefono']
            Cantidad = form.cleaned_data['Cantidad']
            Detalles = form.cleaned_data['Detalles']

            datos = Pedidos(Moneda=Moneda,Solicitante=Solicitante,Empresa=Empresa,Direccion=Direccion,Telefono=Telefono,Cantidad=Cantidad,Detalles=Detalles)
            datos.save()
            return redirect('web:dashboard')
        else:
            print(form.errors)
            print("no funciona")
    else:
        form = Pedido()
        print("Formulario no válido")
        print(form.errors)
          
    
    context = {
        'form': form,
    }

    return render(request, "dashboard.html", context)