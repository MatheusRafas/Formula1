from rest_framework import serializers
from .models import Carro, Equipe, Piloto

class CarroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Carro
    fields ='__all__'

class EquipeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Equipe
    fields ='__all__'

class PilotoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Piloto
    fields ='__all__'