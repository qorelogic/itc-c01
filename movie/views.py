from django.shortcuts import render

# Create your views here.
from movie.models import Movie
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from movie.serializers import MovieSerializer
 
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    def get_queryset(self):
        return Movie.objects.all().filter(user=self.request.user)

