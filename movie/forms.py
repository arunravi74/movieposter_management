from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.layout import Submit
from movie.models import Movie

class user_registration_form(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class MoviePosterForm(forms.ModelForm):
    movie_poster = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Movie
        fields = ['movie_name','movie_description','movie_poster']
        