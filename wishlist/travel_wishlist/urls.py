from django.conf.urls import url
from . import views
#paths for each view (place_list, places_visited,place_is_visited)
urlpatterns = [
    url(r'^$', views.place_list, name='place_list'),
    url(r'^visited$', views.places_visited, name='places_visited'),
    url(r'^isvisited$', views.place_is_visited, name='place_is_visited'),
    url(r'^place_to_visit/(?P<pk>\d+)$', views.place_to_visit, name='place_to_visit'),
]
