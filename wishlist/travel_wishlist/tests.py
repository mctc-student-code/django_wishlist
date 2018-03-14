from django.test import TestCase
from django.urls import reverse

from .models import Place

class TestViewHomePageIsEmptyList(TestCase):

    def test_load_home_page_shows_empty_list(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertFalse(response.context['places'])  #Empty lists are false

# Create your tests here.
class TestWishList(TestCase):
    fixtures = ['test_places']

    def test_view_wishlist(self):
        response = self.client.get(reverse('place_list'))
        #check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        #what data was sent to the template?
        data_rendered = list(response.context['places'])
        #what data is in the database? Get all of the items where visited = False
        data_expected = list(Place.objects.filter(visited=False))
        #is it the same?
        self.assertCountEqual(data_rendered, data_expected)
