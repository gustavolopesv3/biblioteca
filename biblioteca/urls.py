from django.contrib import admin
from django.urls import path
from cadastro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('pesquisa_livro/', pesquisa_livro, name='pesquisa_livro'),
    path('contador/<numero>', contador),
    path('tabela/', tabela),
    path('cadastrosocio', cadastrosocio, name='cadastrosocio'),
    path('socios/', socioslist, name='socios'),


]