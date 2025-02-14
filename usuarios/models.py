from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('aprendiz', 'Aprendiz'),
        ('bienestar', 'Bienestar'),
    )
    rol = models.CharField(max_length=20, choices=ROLES, default='aprendiz')
    horas_acumuladas = models.PositiveIntegerField(default=0)

    # Personaliza los related_name para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_groups',  # Nombre único
        blank=True,
        help_text='Grupos a los que pertenece el usuario.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_permissions',  # Nombre único
        blank=True,
        help_text='Permisos específicos para este usuario.',
    )

    def __str__(self):
        return self.username