from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import Actor, Director, Award, Studio, Film


# Create your forms here

class ActorAddForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    birthdate = forms.DateField(label='Birthdate:')
    nationality = forms.CharField(label='Nationality:', max_length=70)
    height = forms.IntegerField(label='Height:')
    awards = forms.ModelMultipleChoiceField(label='Awards:', queryset=Award.objects.all(), required=False)
    biography = forms.CharField(label='Biography:', widget=forms.Textarea(attrs={'rows': 4}))
    image = forms.FileField(label='Image:', widget=forms.FileInput(attrs={'accept': 'image/*'}))


class DirectorAddForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    birthdate = forms.DateField(label='Birthdate:')
    nationality = forms.CharField(label='Nationality:', max_length=70)
    awards = forms.ModelMultipleChoiceField(label='Awards:', queryset=Award.objects.all(), required=False)
    image = forms.FileField(label='Image:', widget=forms.FileInput(attrs={'accept': 'image/*'}))


class FilmAddForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = ['title', 'director', 'actors', 'studio', 'release_date', 'awards', 'description', 'image', 'trailer']


class StudioAddForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    creation_date = forms.DateField(label='Creation date:')
    ceo = forms.CharField(label='CEO:', max_length=70)


class AwardAddForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=200)
    year = forms.IntegerField(label='Year:')


class CreateAccountForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ReviewForm(forms.Form):
    review = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4}))


class GradeForm(forms.Form):
    grade = forms.ChoiceField(choices=list(zip(range(1, 11), range(1, 11))))


class SearchForm(forms.Form):
    query = forms.CharField(label='Search:', max_length=100)
