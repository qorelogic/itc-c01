
from rest_framework import serializers
 
from movie.models import Movie
 
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
 
    class Meta:
        model = Movie
        #fields = ('url', 'id', 'created', 'name', 'user')
        fields = ('url', 'id', 'created', 'user', 'title', 'releaseYear', 'casting', 'directors', 'producers')
        extra_kwargs = {
            'url': {
                'view_name': 'movie:todo-detail',
            }
        }
