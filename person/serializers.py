
from rest_framework import serializers
 
from person.models import Person
 
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
 
    class Meta:
        model = Person
        #fields = ('url', 'id', 'created', 'user', 'firstName', 'lastName', 'aliases', 'moviesAsActorActress', 'moviesAsDirector', 'moviesAsProducer')
        fields = ('url', 'created', 'user', 'firstName', 'lastName', 'aliases', 'moviesAsActorActress', 'moviesAsDirector', 'moviesAsProducer')
        extra_kwargs = {
            'url': {
                'view_name': 'person:person-detail',
            }
        }
