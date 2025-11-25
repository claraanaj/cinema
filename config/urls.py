from django.contrib import admin
from django.urls import path
from app.views import editar_continente
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('filmes/', FilmesView.as_view(), name='filmes'),
    path('series/', SeriesView.as_view(), name='series'),
    path('generos/', GenerosView.as_view(), name='generos'),
    path('atores/', AtoresView.as_view(), name='atores'),
    path('diretores/', DiretoresView.as_view(), name='diretores'),
    path('paises/', PaisesView.as_view(), name='paises'),
    path('continentes/', ContinentesView.as_view(), name='continentes'),
    path('temporadas/', TemporadasView.as_view(), name='temporadas'),
    path('episodios/', EpisodiosView.as_view(), name='episodios'),
    path('filmes-atores/', FilmesAtoresView.as_view(), name='filmes_atores'),
    path('series-episodios/', SeriesEpisodiosView.as_view(), name='series_episodios'),
    
    # URLs de DELETE
    path('delete-filme/<int:id>/', DeleteFilmeView.as_view(), name='delete_filme'),
    path('delete-serie/<int:id>/', DeleteSerieView.as_view(), name='delete_serie'),
    path('delete-ator/<int:id>/', DeleteAtorView.as_view(), name='delete_ator'),
    path('delete-diretor/<int:id>/', DeleteDiretorView.as_view(), name='delete_diretor'),
    path('delete-genero/<int:id>/', DeleteGeneroView.as_view(), name='delete_genero'),
    path('delete-pais/<int:id>/', DeletePaisView.as_view(), name='delete_pais'),
    path('delete-continente/<int:id>/', DeleteContinenteView.as_view(), name='delete_continente'),
    
    # URLs de EDITAR
    path('editar-filme/<int:id>/', EditarFilmeView.as_view(), name='editar_filme'),
    path('editar-serie/<int:id>/', EditarSerieView.as_view(), name='editar_serie'),
    path('editar-ator/<int:id>/', EditarAtorView.as_view(), name='editar_ator'),
    path('editar-diretor/<int:id>/', EditarDiretorView.as_view(), name='editar_diretor'),
    path('editar-continente/<int:id>/', editar_continente, name='editar_continente'),
]