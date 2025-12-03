from django import forms
from .models import Filme, Serie, Ator, Diretor, Genero, Pais, Continente, Temporada, Episodio, FilmeAtor


class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'


class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'


class AtorForm(forms.ModelForm):
    class Meta:
        model = Ator
        fields = '__all__'


class DiretorForm(forms.ModelForm):
    class Meta:
        model = Diretor
        fields = '__all__'


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'


class ContinenteForm(forms.ModelForm):
    class Meta:
        model = Continente
        fields = '__all__'


class TemporadaForm(forms.ModelForm):
    class Meta:
        model = Temporada
        fields = '__all__'


class EpisodioForm(forms.ModelForm):
    class Meta:
        model = Episodio
        fields = '__all__'


class FilmeAtorForm(forms.ModelForm):
    class Meta:
        model = FilmeAtor
        fields = '__all__'