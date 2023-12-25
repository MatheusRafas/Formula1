from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from formulaum.models import Carro, Equipe, Piloto

class CarroAdmin(ModelAdmin):
  fields = ['modelo', 'placa', 'ano', 'cor', 'equipe', 'feita_manutencao', 'observacao']
  list_display = ['modelo', 'placa', 'equipe', 'feita_manutencao']
  list_editable = ['feita_manutencao']

class EquipeAdmin(ModelAdmin):
  fields = ['nome', 'pais', 'cidade', 'diretor', 'funcionarios', 'observacao']
  list_display = ['nome', 'pais', 'data_de_ingresso_no_campeonato']

class PilotoAdmin(ModelAdmin):
  fields = ['nome', 'carro', 'equipe', 'data_de_nascimento', 'pais_de_origem', 'cidade_natal', 'observacao']
  list_display = ['nome', 'carro', 'equipe', 'data_de_ingresso_na_equipe']

site.register(Carro, CarroAdmin)
site.register(Equipe, EquipeAdmin)
site.register(Piloto, PilotoAdmin)