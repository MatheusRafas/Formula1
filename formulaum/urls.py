from django.urls.conf import include
from django.urls import path
import formulaum.urls
from formulaum.views import CarroView, CarroDetail, CarroDetailAPI, AdicionaCarro, CarroList
from formulaum.views import EquipeView, EquipeDetail, EquipeDetailAPI, AdicionaEquipe, EquipeList
from formulaum.views import PilotoView, PilotoDetail, AdicionaPiloto, PilotoList, PilotoDetailAPI
from formulaum.views import Home, CriaUsuario

urlpatterns = [
  
  path('', Home.as_view(), name='carro-home'),
  path('criar_usuario/$', CriaUsuario.as_view()),

  # Carro
  path('carros/', CarroView.as_view(), name="carro-view", ),
  path('carros/criar/', AdicionaCarro.as_view()),
  path('carros/<int:pk>/', CarroDetail.as_view(), name="carro-detail", ),

  # Equipe
  path('equipes/', EquipeView.as_view(), name="equipe-view", ),
  path('equipes/criar/', AdicionaEquipe.as_view()),
  path('equipes/<int:pk>/', EquipeDetail.as_view(), name="equipe-detail", ),

  # Piloto
  path('pilotos/', PilotoView.as_view(), name="piloto-view", ),
  path('pilotos/criar/', AdicionaPiloto.as_view()),
  path('pilotos/<int:pk>/', PilotoDetail.as_view(), name="piloto-detail", ),
  
  # URLs epecíficas para a API Rest
  path('carros/v1/', CarroList.as_view(), name='carro-list'),
  path('carros/v1/<int:pk>/', CarroDetailAPI.as_view(), name='carro-detail'),
  path('equipes/v1/', EquipeList.as_view(), name='equipe-list'),
  path('equipes/v1/<int:pk>/', EquipeDetailAPI.as_view(), name='equipe-detail'),
  path('pilotos/v1/', PilotoList.as_view(), name='piloto-list'),
  path('pilotos/v1/<int:pk>/', PilotoDetailAPI.as_view(), name='piloto-detail'),
]