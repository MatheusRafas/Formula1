from django.template import context, RequestContext
from django.views.generic import View
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from rest_framework import generics
from formulaum.forms import FormNovoUsuario, FormCarro, FormEquipe, FormPiloto
from formulaum.models import Carro, Equipe, Piloto
from formulaum.serializers import CarroSerializer, EquipeSerializer, PilotoSerializer
from rest_framework.permissions import IsAuthenticated

class Home(View):
  template_name = 'formulaum/home.html'
  context = {}
  def get(self, request, *args, **kwargs):
    self.context['counter'] = Carro.objects.filter(feita_manutencao=False).count()
    return render(request, 'formulaum/home.html', self.context)
    
class CriaUsuario(View):
  template_name = 'formulaum/cria_usuario.html'
  context = {}

  def get(self, request, *args, **kwargs):
      self.context['form'] = FormNovoUsuario()
      return render(request, self.template_name, self.context)

  def post(self, request, *args, **kwargs):
      form = FormNovoUsuario(request.POST)

      if form.is_valid():
          form.save()
          return redirect('/')
      else:
          self.context['form'] = form
          return render(request, self.template_name, self.context)

class CarroView(ArchiveIndexView):
  model = Carro
  date_field = 'data_de_compra'

class EquipeView(ArchiveIndexView):
  model = Equipe
  date_field = 'data_de_ingresso_no_campeonato'

class PilotoView(ArchiveIndexView):
  model = Piloto
  date_field = 'data_de_ingresso_na_equipe'

class CarroDetail(DetailView):
  model = Carro

class EquipeDetail(DetailView):
  model = Equipe

class PilotoDetail(DetailView):
  model = Piloto

class CarroDetailAPI(generics.RetrieveUpdateDestroyAPIView):
  queryset = Carro.objects.all()
  serializer_class = CarroSerializer

class EquipeDetailAPI(generics.RetrieveUpdateDestroyAPIView):
  queryset = Equipe.objects.all()
  serializer_class = EquipeSerializer

class PilotoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
  queryset = Piloto.objects.all()
  serializer_class = PilotoSerializer

class AdicionaCarro(View):
  template_name = 'formulaum/cria_carro.html'
  context = {}

  def get(self, request, *args, **kwargs):
      self.context['form'] = FormCarro()
      return render(request, self.template_name, self.context)

  def post(self, request, *args, **kwargs):
      form = FormCarro(request.POST)

      if form.is_valid():
          form.save()
          return redirect('/carros/')
      else:
          self.context['form'] = form

      return render(request, self.template_name, self.context)

class AdicionaEquipe(View):

  template_name = 'formulaum/cria_equipe.html'
  context= {}

  def get(self, request, *args, **kwargs):
      self.context['form'] = FormEquipe()
      return render(request, self.template_name, self.context)

  def post(self, request, *args, **kwargs):
      form = FormEquipe(request.POST)

      if form.is_valid():
          form.save()
          return redirect('/equipes/')
      else:
          self.context['form'] = form
          return render(request, self.template_name, self.context)

class AdicionaPiloto(View):
  template_name = 'formulaum/cria_piloto.html'
  context = {}

  def get(self, request, *args, **kwargs):
    self.context['form'] = FormPiloto()
    return render(request, self.template_name, self.context)

  def post(self, request, *args, **kwargs):
    form = FormPiloto(request.POST)
  
    if form.is_valid():
      form.save()
      return redirect('/pilotos/')
    else:
      self.context['form'] = form
      return render(request, self.template_name, self.context)
    
class CarroList(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  #queryset = Carro.objects.all()
  serializer_class = CarroSerializer
  
  def get_queryset(self):
  
    manut_param = self.request.query_params.get('feita_manutencao', None)
    queryset = Carro.objects.all()
  
    if manut_param:
      queryset = queryset.filter(feita_manutencao=manut_param)
  
    return queryset

class EquipeList(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = EquipeSerializer

  def get_queryset(self):

    pais_param = self.request.query_params.get('pais', None)
    queryset = Equipe.objects.all()

    if pais_param:
      queryset = queryset.filter(pais=pais_param)

    return queryset

class PilotoList(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  #queryset = Piloto.objects.all()
  serializer_class = PilotoSerializer

  def get_queryset(self):
    nome_param = self.request.query_params.get('nome', None)
    queryset = Piloto.objects.all()
    
    if nome_param:
      queryset = queryset.filter(nome=nome_param)
      
    return queryset