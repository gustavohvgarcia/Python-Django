from django.contrib import admin
from .models import Funcionario

# Register your models here.


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        "primeiroNome",
        "ultimoNome",
        "dataAdmissao",
    )


admin.site.register(Funcionario, FuncionarioAdmin)
