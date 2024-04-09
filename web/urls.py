from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name='web'

urlpatterns=[
    path('login/', views.login, name="login"),   
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('', views.inicio, name="inicio"),
    path('registro/', views.registro, name="registro"),
    path('ordenes-cliente/', views.ordenes, name="ordenes-cliente"),
    path('aceptar-ordenes/', views.aceptar_ordenes, name="aceptar-ordenes"),
    path('reenvio-orden/', views.reenvio_orden, name="reenvio-orden"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

