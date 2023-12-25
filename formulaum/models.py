from django.db.models import Model, ForeignKey
from django.db.models import BooleanField, CharField, DateTimeField, TextField
from django.db import models

class Equipe(Model):
    nome = CharField(max_length=50)
    data_de_ingresso_no_campeonato = DateTimeField(
        auto_now_add=True, verbose_name='Data de ingresso no campeonato')
    pais = CharField(max_length=100)
    cidade = CharField(max_length=200, null=True, blank=True)
    diretor = CharField(max_length=200, null=True, blank=True)
    funcionarios = CharField(max_length=200, null=True, blank=True)
    observacao = TextField(null=True, blank=True)
  
    def __str__(self):
      return self.nome

    class Meta:
      ordering = ['-data_de_ingresso_no_campeonato']


class Carro(Model):
    modelo = CharField(max_length=50)
    placa = CharField(max_length=10)
    ano = CharField(max_length=4, null=True, blank=True)
    cor = CharField(max_length=50, null=True, blank=True)
    equipe = ForeignKey(Equipe, on_delete=models.CASCADE)
    data_de_compra = DateTimeField(auto_now_add=True,
                                   verbose_name='Data de compra')
    feita_manutencao = BooleanField(default=False,
                                    verbose_name='Foi feita manutenção?')
    observacao = TextField(null=True, blank=True)

    def __str__(self):
      return self.modelo + ' | Placa ' + self.placa

    class Meta:
      ordering = ['-data_de_compra']


class Piloto(Model):
    nome = CharField(max_length=50)
    carro = ForeignKey(Carro, on_delete=models.CASCADE)
    equipe = ForeignKey(Equipe, on_delete=models.CASCADE)
    data_de_ingresso_na_equipe = DateTimeField(
        auto_now_add=True, verbose_name='Data de ingresso na equipe')
    data_de_nascimento = DateTimeField(verbose_name='Data Nascimento',
         null=True, blank=True)
    pais_de_origem = CharField(max_length=100)
    cidade_natal = CharField(max_length=100, null=True, blank=True)
    observacao = TextField(null=True, blank=True)

    class Meta:
      ordering = ['-data_de_ingresso_na_equipe']