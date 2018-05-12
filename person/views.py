from django.shortcuts import render

# Create your views here.
from person.models import Person
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from person.serializers import PersonSerializer
 
class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
 
class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
 
    def get_queryset(self):
        return Person.objects.all().filter(username=self.request.user)

