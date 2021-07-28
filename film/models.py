from django.db import models
from django.core.validators import validate_slug
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your models here.

class categories(models.Model):
    name = models.CharField(max_length=50,validators=[validate_slug])
    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=20,validators=[validate_slug])
    def __str__(self):
        return self.name

class actors(models.Model):
    name = models.CharField(max_length=40)

class origin(models.Model):
    name = models.CharField(max_length=30)

class film(models.Model):
    title = models.CharField(max_length=50, validators=[validate_slug])
    director = models.ForeignKey(Director, related_name='director', on_delete=models.CASCADE)
    origins = models.ForeignKey(origin, related_name='origin', on_delete=models.CASCADE)
    actor = models.ManyToManyField(actors, through='acotors_film')
    review = models.ManyToManyField(User, through='review_of_film', related_name='review_of_film')
    interact = models.ManyToManyField(User, through='like_un_like_film', related_name='like_un_like_film')
    search = models.ManyToManyField(User, through='search_history', related_name='search_history')
    categorie = models.ManyToManyField(categories, through='categories_film', related_name='categories_film')
    production_company = models.CharField(max_length=60,null=True)
    description = models.CharField(max_length=9000)
    release_date = models.DateField(auto_now_add=True)
    run_time = models.IntegerField()
    spoken_language = models.CharField(max_length=50,null=True)
    rate = models.IntegerField()
    link_of_film = models.CharField(max_length=200,null=True)

class review_of_film(models.Model):
    users = models.ForeignKey(User, related_name='nameUser', on_delete=models.CASCADE)
    films = models.ForeignKey(film, related_name="namefileUser", on_delete=models.CASCADE)
    times_tamp = models.DateField(null=True)
    precent_rate = models.IntegerField()

class search_history(models.Model):
    users = models.ForeignKey(User,related_name='search',on_delete=models.CASCADE)
    films = models.ForeignKey(film, related_name="searchuser", on_delete=models.CASCADE)
    Text = models.CharField(max_length=9000)
    chosen_or_not = models.IntegerField()

class like_un_like_film(models.Model):
    users = models.ForeignKey(User , related_name='makelike' ,on_delete=models.CASCADE)
    films = models.ForeignKey(film,related_name='namefile',on_delete=models.CASCADE)
    true_or_not = models.IntegerField()

class acotors_film(models.Model):
      films = models.ForeignKey(film, related_name='films', on_delete=models.CASCADE)
      actors = models.ForeignKey(actors, related_name='actor', on_delete=models.CASCADE)

class categories_film(models.Model):
    films = models.ForeignKey(film, related_name='filmsCategories', on_delete=models.CASCADE)
    categori = models.ForeignKey(categories, related_name='categori', on_delete=models.CASCADE)