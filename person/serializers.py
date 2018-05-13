
from rest_framework import serializers
 
from person.models import Person
 
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
 
    class Meta:
        model = Person
        fields = ('url', 'id', 'created', 'name', 'user')
        extra_kwargs = {
            'url': {
                'view_name': 'person:todo-detail',
            }
        }
