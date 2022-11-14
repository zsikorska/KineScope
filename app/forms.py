from django import forms

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