from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMINISTRADOR = 'ADMIN', 'Administrador'
        FUNCIONARIO = 'FUNC', 'Funcionario'
        OPERADOR = 'OPER', 'Operador'

    role = models.CharField(
        max_length=5,
        choices=Role.choices,
        default=Role.OPERADOR,
    )

    def is_administrador(self):
        return self.role == self.Role.ADMINISTRADOR

    def is_funcionario(self):
        return self.role == self.Role.FUNCIONARIO

    def is_operador(self):
        return self.role == self.Role.OPERADOR
