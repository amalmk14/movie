from django import forms
from .models import Movie

class MvieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','year','desc','img']