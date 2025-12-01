from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *
from .forms import *


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class FilmesView(View):
    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.all()
        return render(request, 'filmes.html', {'filmes': filmes})


class SeriesView(View):
    def get(self, request, *args, **kwargs):
        series = Serie.objects.all()
        return render(request, 'series.html', {'series': series})


class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'generos.html', {'generos': generos})


class AtoresView(View):
    def get(self, request, *args, **kwargs):
        atores = Ator.objects.all()
        return render(request, 'atores.html', {'atores': atores})


class DiretoresView(View):
    def get(self, request, *args, **kwargs):
        diretores = Diretor.objects.all()
        return render(request, 'diretores.html', {'diretores': diretores})


class PaisesView(View):
    def get(self, request, *args, **kwargs):
        paises = Pais.objects.all()
        return render(request, 'paises.html', {'paises': paises})


class ContinentesView(View):
    def get(self, request, *args, **kwargs):
        continentes = Continente.objects.all()
        return render(request, 'continentes.html', {'continentes': continentes})


class TemporadasView(View):
    def get(self, request, *args, **kwargs):
        temporadas = Temporada.objects.all()
        return render(request, 'temporadas.html', {'temporadas': temporadas})


class EpisodiosView(View):
    def get(self, request, *args, **kwargs):
        episodios = Episodio.objects.all()
        return render(request, 'episodios.html', {'episodios': episodios})


class FilmesAtoresView(View):
    def get(self, request, *args, **kwargs):
        filmes_atores = FilmeAtor.objects.all()
        return render(request, 'filmes_atores.html', {'filmes_atores': filmes_atores})


class SeriesEpisodiosView(View):
    def get(self, request, *args, **kwargs):
        series_episodios = SerieEpisodio.objects.all()
        return render(request, 'series_episodios.html', {'series_episodios': series_episodios})


class DeleteFilmeView(View):
    def get(self, request, id, *args, **kwargs):
        filme = Filme.objects.get(id=id)
        filme.delete()
        messages.success(request, 'Filme excluído com sucesso!')
        return redirect('filmes')


class DeleteSerieView(View):
    def get(self, request, id, *args, **kwargs):
        serie = Serie.objects.get(id=id)
        serie.delete()
        messages.success(request, 'Série excluída com sucesso!')
        return redirect('series')


class DeleteAtorView(View):
    def get(self, request, id, *args, **kwargs):
        ator = Ator.objects.get(id=id)
        ator.delete()
        messages.success(request, 'Ator excluído com sucesso!')
        return redirect('atores')


class DeleteDiretorView(View):
    def get(self, request, id, *args, **kwargs):
        diretor = Diretor.objects.get(id=id)
        diretor.delete()
        messages.success(request, 'Diretor excluído com sucesso!')
        return redirect('diretores')


class DeleteGeneroView(View):
    def get(self, request, id, *args, **kwargs):
        genero = Genero.objects.get(id=id)
        genero.delete()
        messages.success(request, 'Gênero excluído com sucesso!')
        return redirect('generos')


class DeletePaisView(View):
    def get(self, request, id, *args, **kwargs):
        pais = Pais.objects.get(id=id)
        pais.delete()
        messages.success(request, 'País excluído com sucesso!')
        return redirect('paises')


class DeleteContinenteView(View):
    def get(self, request, id, *args, **kwargs):
        continente = Continente.objects.get(id=id)
        continente.delete()
        messages.success(request, 'Continente excluído com sucesso!')
        return redirect('continentes')


class EditarFilmeView(View):
    template_name = 'editar_filme.html'

    def get(self, request, id, *args, **kwargs):
        filme = get_object_or_404(Filme, id=id)
        form = FilmeForm(instance=filme)
        return render(request, self.template_name, {'filme': filme, 'form': form})

    def post(self, request, id, *args, **kwargs):
        filme = get_object_or_404(Filme, id=id)
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filme editado com sucesso!')
            return redirect('editar_filme', id=id)
        else:
            messages.error(request, 'Corrija os erros no formulário.')
        return render(request, self.template_name, {'filme': filme, 'form': form})


class EditarSerieView(View):
    template_name = 'editar_serie.html'

    def get(self, request, id, *args, **kwargs):
        serie = get_object_or_404(Serie, id=id)
        form = SerieForm(instance=serie)
        return render(request, self.template_name, {'serie': serie, 'form': form})

    def post(self, request, id, *args, **kwargs):
        serie = get_object_or_404(Serie, id=id)
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Série editada com sucesso!')
            return redirect('editar_serie', id=id)
        else:
            messages.error(request, 'Corrija os erros no formulário.')
        return render(request, self.template_name, {'serie': serie, 'form': form})


class EditarAtorView(View):
    template_name = 'editar_ator.html'

    def get(self, request, id, *args, **kwargs):
        ator = get_object_or_404(Ator, id=id)
        form = AtorForm(instance=ator)
        return render(request, self.template_name, {'ator': ator, 'form': form})

    def post(self, request, id, *args, **kwargs):
        ator = get_object_or_404(Ator, id=id)
        form = AtorForm(request.POST, instance=ator)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ator editado com sucesso!')
            return redirect('editar_ator', id=id)
        else:
            messages.error(request, 'Corrija os erros no formulário.')
        return render(request, self.template_name, {'ator': ator, 'form': form})


class EditarDiretorView(View):
    template_name = 'editar_diretor.html'

    def get(self, request, id, *args, **kwargs):
        diretor = get_object_or_404(Diretor, id=id)
        form = DiretorForm(instance=diretor)
        return render(request, self.template_name, {'diretor': diretor, 'form': form})

    def post(self, request, id, *args, **kwargs):
        diretor = get_object_or_404(Diretor, id=id)
        form = DiretorForm(request.POST, instance=diretor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Diretor editado com sucesso!')
            return redirect('editar_diretor', id=id)
        else:
            messages.error(request, 'Corrija os erros no formulário.')
        return render(request, self.template_name, {'diretor': diretor, 'form': form})


class EditarContinenteView(View):
    template_name = 'editar_continente.html'

    def get(self, request, id, *args, **kwargs):
        continente = get_object_or_404(Continente, id=id)
        form = ContinenteForm(instance=continente)
        return render(request, self.template_name, {'continente': continente, 'form': form})

    def post(self, request, id, *args, **kwargs):
        continente = get_object_or_404(Continente, id=id)
        form = ContinenteForm(request.POST, instance=continente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Continente editado com sucesso!')
            return redirect('editar_continente', id=id)
        else:
            messages.error(request, 'Corrija os erros no formulário.')
        return render(request, self.template_name, {'continente': continente, 'form': form})