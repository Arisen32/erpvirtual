from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login , authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import Register ,LoginForm, Pedido
from .models import Usuario, Pedidos
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.core.paginator import Paginator



def inicio(request):
    
    context={}
    return render(request, "inicio.html", context)




def registro(request):
    if request.method == 'POST':
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

            # Verificar si el checkbox de cliente está seleccionado
            is_cliente = 'clienteCheckbox' in request.POST

            # Verificar si el checkbox de proveedor está seleccionado
            is_proveedor = 'proveedorCheckbox' in request.POST

            # Hash de la contraseña
            hashed_password = make_password(password)

            # Crear el usuario y guardar
            usuario = Usuario(RazonS=RazonS, DireccionF=DireccionF, CodigoP=CodigoP, RFC=RFC, DireccionE=DireccionE, email=email, username=username, password=hashed_password, is_cliente=is_cliente, is_Proveedor=is_proveedor)
            usuario.save()

            return redirect('web:login')

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

            pedido = Pedidos(Moneda=Moneda, Solicitante=Solicitante, Empresa=Empresa, Direccion=Direccion, Telefono=Telefono, Cantidad=Cantidad, Detalles=Detalles)
            pedido.save()

            return redirect('web:dashboard')

        
    else:
        form = Pedido()
          
    
    context = {
        'form': form,
    }

    return render(request, "dashboard.html", context)



def ordenes(request):
    
    pedidos_list = Pedidos.objects.all()
    paginator = Paginator(pedidos_list, 3)
    pagina = request.GET.get("ordenes-cliente") or 1
    posts = paginator.get_page(pagina)
    current_page = int(pagina)
    paginas = range(1, posts.paginator.num_pages + 1)
    

    context = {
        'pedidos': posts,
        'paginas': paginas,
        'current_page': current_page
    }

    return render(request, "ordenes-cliente.html", context)