from django.db import models

# Create your models here.
class Funcionario(models.Model):
    primeiroNome = models.CharField(max_length=255)
    ultimoNome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    salario = models.FloatField()
    dataAdmissao = models.DateField()
    dataNascimento = models.DateField(null=True)
    telefone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)

    # sobrescrita do método __str__ para retornar o nome do funcionario
    # ao invés de "Member Object (indice)]"
    def __str__(self):
        return f"{self.primeiroNome} {self.ultimoNome}"
