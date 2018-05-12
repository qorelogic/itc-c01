
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from movie import views
 
urlpatterns = [
     url(r'^movie/$', views.MovieList.as_view(), name='movie-list'),
     url(r'^movie/(?P<pk>[0-9]+)/$', views.MovieDetail.as_view(), name='movie-detail'),
]

