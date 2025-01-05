from django.contrib import admin
from django.urls import path
from app_gestaopessoal import views

urlpatterns = [
 path('admin/', admin.site.urls),
 # rota, view responsável, nome de referência
 # estrategiandomarketing.com
 path('', views.home, name='home'),
 # estrategiandomarketing.com/usuarios
 path('usuarios/', views.usuarios, name='listagem_usuarios')
 

]
