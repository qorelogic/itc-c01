from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
       'users': reverse('users:user-list', request=request, format=format),
       'person': reverse('person:person-list', request=request, format=format),
       'movie': reverse('movie:movie-list', request=request, format=format),
    })
