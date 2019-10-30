# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from cadastro.models import *
from cadastro.forms import *


def index(request):

    return render(request, 'index.html', locals())


def pesquisa_livro(request):
    valor_pesquisa = request.GET.get('campo_busca')
    resultados = None
    return render(request, 'pesquisa_livro.html', locals())


def contador(request, numero):
    numeros = range(0, int(numero))

    return render(request, 'contador.html', locals())


def tabela(request):
    livro = {
        ('Culpa das Estrelas', 'Roberto', 2015, 1, 'Abril', 1),
        ('A cabana', 'Marcelo', 2016, 2, 'Globo', 1)
    }
    return render(request, 'tabela.html', locals())


def socioslist(request):
    socio = Socio.objects.all()
    return render(request, 'socios.html', locals())


def cadastrosocio(request):
    form = FormSocio()
    if request.method == "POST":
        form = FormSocio(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('socios'))
    return render(request, 'cadastrosocio.html', locals())