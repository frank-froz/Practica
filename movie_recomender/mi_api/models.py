from django.db import models

class GenreDB(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Genre'
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class MovieDB(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(null=True, blank=True)
    plot = models.TextField(blank=True)
    runtime = models.PositiveIntegerField(help_text="Duración en minutos", null=True, blank=True)
    imdb_id = models.CharField("ID de IMDb", max_length=20, blank=True)
    genres = models.ManyToManyField(GenreDB, related_name='movies')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Movie'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
