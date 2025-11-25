from django.contrib import admin
from .models import *


# Inlines conforme requisitos do projeto
class PaisInline(admin.TabularInline):
    model = Pais
    extra = 1


class FilmeAtorInline(admin.TabularInline):
    model = FilmeAtor
    extra = 1


class SerieEpisodioInline(admin.TabularInline):
    model = SerieEpisodio
    extra = 1


class EpisodioInline(admin.TabularInline):
    model = Episodio
    extra = 1


# Configuração dos Admins com Inlines
@admin.register(Continente)
class ContinenteAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    inlines = [PaisInline]


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['nome', 'continente']
    search_fields = ['nome']
    list_filter = ['continente']


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nacionalidade', 'insta', 'twitter']
    search_fields = ['nome', 'nacionalidade']
    list_filter = ['nacionalidade']


@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nacionalidade', 'insta', 'twitter']
    search_fields = ['nome', 'nacionalidade']
    list_filter = ['nacionalidade']


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'diretor', 'genero', 'pais', 'data_lancamento', 'nota_avaliacao']
    search_fields = ['nome', 'diretor__nome']
    list_filter = ['genero', 'pais', 'data_lancamento']
    inlines = [FilmeAtorInline]


@admin.register(FilmeAtor)
class FilmeAtorAdmin(admin.ModelAdmin):
    list_display = ['filme', 'ator']
    search_fields = ['filme__nome', 'ator__nome']
    list_filter = ['filme', 'ator']


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ['nome', 'diretor', 'genero', 'pais', 'data_lancamento', 'nota_avaliacao']
    search_fields = ['nome', 'diretor__nome']
    list_filter = ['genero', 'pais', 'data_lancamento']
    inlines = [SerieEpisodioInline]


@admin.register(Temporada)
class TemporadaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    inlines = [SerieEpisodioInline]


@admin.register(Episodio)
class EpisodioAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(SerieEpisodio)
class SerieEpisodioAdmin(admin.ModelAdmin):
    list_display = ['serie', 'temporada', 'episodio', 'duracao', 'data_disponibilizacao']
    search_fields = ['serie__nome', 'episodio__nome']
    list_filter = ['serie', 'temporada', 'data_disponibilizacao']