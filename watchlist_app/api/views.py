from watchlist_app.models import Movie
from rest_framework.response import Response
from watchlist_app.api.serializers import Moviserializer
from django.http import HttpResponse
from rest_framework.decorators import api_view

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = Moviserializer(movies)
    return Response(serializer.data)
    
@api_view()
def movie_details(rqueste,pk):
    movie = Movie.objects.all(pk=pk)
    serializer = Moviserializer(movie)
    return Response(serializer.data)

