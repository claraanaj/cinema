from django.db import models


class Continente(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do continente")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Continente"
        verbose_name_plural = "Continentes"


class Pais(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do país")
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE, verbose_name="Continente")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"


class Genero(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do gênero")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"


class Ator(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do ator")
    site = models.URLField(verbose_name="Site", blank=True)
    insta = models.CharField(max_length=100, verbose_name="Instagram", blank=True)
    face = models.CharField(max_length=100, verbose_name="Facebook", blank=True)
    twitter = models.CharField(max_length=100, verbose_name="Twitter", blank=True)
    nacionalidade = models.CharField(max_length=100, verbose_name="Nacionalidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ator"
        verbose_name_plural = "Atores"


class Diretor(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do diretor")
    site = models.URLField(verbose_name="Site", blank=True)
    insta = models.CharField(max_length=100, verbose_name="Instagram", blank=True)
    face = models.CharField(max_length=100, verbose_name="Facebook", blank=True)
    twitter = models.CharField(max_length=100, verbose_name="Twitter", blank=True)
    nacionalidade = models.CharField(max_length=100, verbose_name="Nacionalidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Diretor"
        verbose_name_plural = "Diretores"


class Filme(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do filme")
    duracao = models.IntegerField(verbose_name="Duração (minutos)")
    sinopse = models.TextField(verbose_name="Sinopse")
    site_oficial = models.URLField(verbose_name="Site oficial", blank=True)
    data_lancamento = models.DateField(verbose_name="Data de lançamento")
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Nota de avaliação")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Gênero")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="País")
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE, verbose_name="Diretor")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"


class FilmeAtor(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, verbose_name="Filme")
    ator = models.ForeignKey(Ator, on_delete=models.CASCADE, verbose_name="Ator")

    def __str__(self):
        return f"{self.filme.nome} - {self.ator.nome}"

    class Meta:
        verbose_name = "Filme com Ator"
        verbose_name_plural = "Filmes com Atores"


class Serie(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome da série")
    duracao = models.IntegerField(verbose_name="Duração média episódio (minutos)")
    sinopse = models.TextField(verbose_name="Sinopse")
    site_oficial = models.URLField(verbose_name="Site oficial", blank=True)
    data_lancamento = models.DateField(verbose_name="Data de lançamento")
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Nota de avaliação")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Gênero")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="País")
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE, verbose_name="Diretor")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Série"
        verbose_name_plural = "Séries"


class Temporada(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da temporada")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"


class Episodio(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do episódio")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Episódio"
        verbose_name_plural = "Episódios"


class SerieEpisodio(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, verbose_name="Série")
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE, verbose_name="Temporada")
    episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE, verbose_name="Episódio")
    duracao = models.IntegerField(verbose_name="Duração (minutos)")
    data_disponibilizacao = models.DateField(verbose_name="Data de disponibilização")

    def __str__(self):
        return f"{self.serie.nome} - {self.temporada.nome} - {self.episodio.nome}"

    class Meta:
        verbose_name = "Série com Episódio"
        verbose_name_plural = "Séries com Episódios"