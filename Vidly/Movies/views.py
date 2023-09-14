from django.shortcuts import render,get_object_or_404
from .models import Movie
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    output = ",".join([movie.title for movie in movies ])
    return render(request,"Movies/Movies.html",{"movies":movies})

def details(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request,"Movies/Movies_details.html",{"movie":movie})