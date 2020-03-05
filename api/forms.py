from django import forms

# form to search for movies by title

class MovieForm(forms.Form):
    movie_name = forms.CharField(label='Movie name', max_length=200)

# form to search for movies by rating cutoff

class RatingForm(forms.Form):
    imdb_rating = forms.FloatField(label='Rating')