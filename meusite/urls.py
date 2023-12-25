from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from formulaum.views import CriaUsuario
import formulaum.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('formulaum.urls', 'formulaum'), namespace='formulaum')),
    path('criar_usuario/$', CriaUsuario.as_view()),
    path('api/', include('formulaum.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]