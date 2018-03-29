from django import forms
from .models import Place
# main form
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'visited')

class Place_to_visit_form(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('date_visited', 'note')
