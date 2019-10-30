
from django.db import models

class Socio(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=14)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField('Título', max_length=120)
    ano_edicao = models.CharField('Ano Edição', max_length=4)
    edicao = models.IntegerField('Edição')
    situacao  = models.BooleanField('Situação', default=False)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    autor = models.ManyToManyField(Autor)

    def __str__(self):
        return  self.titulo

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    dtemprestimo = models.DateField('Data de Emprestimo')
    dtdevolucao = models.DateField('Data de Devolução')

    def __str__(self):
        return self.livro.titulo
