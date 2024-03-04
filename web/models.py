from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    RazonS = models.CharField(max_length=150)
    DireccionF = models.CharField(max_length=200)
    CodigoP = models.CharField(max_length=50)
    RFC = models.CharField(max_length=50)
    DireccionE = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',  # Cambiado el related_name
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_user_permissions',  # Cambiado el related_name
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.email
    
    
class Pedidos(models.Model):
    Moneda = models.CharField(max_length=50)
    Solicitante = models.CharField(max_length=120)
    Empresa = models.CharField(max_length=200)
    Direccion = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=100)  
    Cantidad = models.CharField(max_length=100) 
    Detalles = models.CharField(max_length=400)    