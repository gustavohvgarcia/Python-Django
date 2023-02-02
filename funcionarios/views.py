from django.http import HttpResponse
from django.template import loader
from .models import Funcionario
from loguru import logger

# Create your views here.


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def funcionarios(request):
    # recupera todos os objetos do banco de dados
    funcionarios_list = Funcionario.objects.all().values()

    # carrega o template afetado pela ação
    template = loader.get_template("listar_funcionarios.html")

    # cria um objeto contendo as informacoes recuperadas da tabela
    context = {"mymembers": funcionarios_list}
    # manda o objeto para o template, exibindo o html na tela
    return HttpResponse(template.render(context, request))


def detalhes(request, id: int):
    # retorna o funcionario com o id passado na url
    funcionario = Funcionario.objects.get(id=id)

    # carrega o template afetado pela ação
    template = loader.get_template("detalhes.html")
    # cria um objeto contendo as informacoes recuperadas da tabela
    context = {
        "mymember": funcionario,
    }

    # manda o objeto para o template, exibindo o html na tela
    return HttpResponse(template.render(context, request))


def testing(request):
    funcionario = Funcionario.objects.all().values()
    template = loader.get_template("template.html")
    context = {
        "mymembers": funcionario,
    }
    return HttpResponse(template.render(context, request))
