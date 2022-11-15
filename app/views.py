from django.db.models import Avg, Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

from app.forms import ActorAddForm, DirectorAddForm, StudioAddForm, AwardAddForm, FilmAddForm, CreateAccountForm, \
    ReviewForm, GradeForm, SearchForm
from app.models import User, Actor, Director, Studio, Award, Film, Grade, Review


# Create views

def home(request):
    films = Film.objects.all().order_by('-release_date')[0:3]

    print(films)

    return render(request, 'index.html', {'films': films})


def actor(request, id_a):
    return render(request, 'actor.html', {'actor': Actor.objects.get(id=id_a)})


def actor(request, id_d):
    return render(request, 'director.html', {'director': Director.objects.get(id=id_d)})


def film(request, id):
    avg = Grade.objects.filter(film__id=id).aggregate(Avg('grade'))['grade__avg']
    if avg is None:
        avg = 0
    avg = round(avg, 2)

    reviews = Review.objects.filter(film__id=id)
    return render(request, 'film.html', {'film': Film.objects.get(id=id), 'grade': avg, 'reviews': reviews,
                                         'form_review': ReviewForm(), 'form_grade': GradeForm()})


# def user(request):
#     tparams = {
#         'title': 'User',
#         'message': 'User page',
#         'year': datetime.now().year,
#     }
#     return render(request, 'user.html', tparams)

# def authorins(request):
#     if not request.user.is_authoricated or request.user.username != 'admin':
#         return redirect('/login')
#     # if POST request, process from data
#     if request.method == 'POST':
#         # create form instance and pass data to it
#         form = UserInsForm(request.POST)
#         if form.is_valid(): # is it valid?
#             username = form.cleaned_data['email']
#             email = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             a = User(email=email, username=username, password=username)
#             a.save()
#             return HttpResponse("<h1>Author Inserted!<h1>")
#     # if GET (or any other method), create black form
#     else:
#         form = UserInsForm()
#     return render(request, 'authorins.html', {'form':form})

def add_film(request):
    # if not request.user.is_authenticated or request.user.username != 'admin':
    #     return redirect('/login')

    if request.method == "POST":
        form = FilmAddForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            director = form.cleaned_data['director']
            actors = form.cleaned_data['actors']
            studio = form.cleaned_data['studio']
            release_date = form.cleaned_data['release_date']
            if not form.cleaned_data['awards']:
                awards = ''
            else:
                awards = form.cleaned_data['awards']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            trailer = form.cleaned_data['trailer']
            film = Film(
                title=title,
                director=director,
                studio=studio,
                release_date=release_date,
                description=description,
                image=image,
                trailer=trailer
                           )
            film.save()
            film.awards.set(awards)
            film.actors.set(actors)
            return redirect('films')
    else:
        form = FilmAddForm()
    return render(request, 'add_film.html', {'form': form})


def add_actor(request):
    # if not request.user.is_authenticated or request.user.username != 'admin':
    #     return redirect('/login')

    if request.method == "POST":
        form = ActorAddForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            birthdate = form.cleaned_data['birthdate']
            nationality = form.cleaned_data['nationality']
            height = form.cleaned_data['height']
            if not form.cleaned_data['awards']:
                awards = ''
            else:
                awards = form.cleaned_data['awards']
            biography = form.cleaned_data['biography']
            image = form.cleaned_data['image']
            actor = Actor(
                name=name,
                birthdate=birthdate,
                nationality=nationality,
                height=height,
                biography=biography,
                image=image
                           )
            actor.save()
            actor.awards.set(awards)
            return redirect('actors')
    else:
        form = ActorAddForm()
    return render(request, 'add_actor.html', {'form': form})


def add_director(request):
    # if not request.user.is_authenticated or request.user.username != 'admin':
    #     return redirect('/login')

    if request.method == "POST":
        form = DirectorAddForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            birthdate = form.cleaned_data['birthdate']
            nationality = form.cleaned_data['nationality']
            if not form.cleaned_data['awards']:
                awards = ''
            else:
                awards = form.cleaned_data['awards']
            image = form.cleaned_data['image']
            director = Director(
                name=name,
                birthdate=birthdate,
                nationality=nationality,
                image=image
                           )
            director.save()
            director.awards.set(awards)
            return redirect('directors')
    else:
        form = DirectorAddForm()
    return render(request, 'add_director.html', {'form': form})


def add_studio(request):
    # if not request.user.is_authenticated or request.user.username != 'admin':
    #     return redirect('/login')

    if request.method == "POST":
        form = StudioAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            creation_date = form.cleaned_data['creation_date']
            ceo = form.cleaned_data['ceo']
            studio = Studio(
                name=name,
                creation_date=creation_date,
                ceo=ceo
                           )
            studio.save()
            return redirect('studios')
    else:
        form = StudioAddForm()
    return render(request, 'add_studio.html', {'form': form})


def add_award(request):
    # if not request.user.is_authenticated or request.user.username != 'admin':
    #     return redirect('/login')

    if request.method == "POST":
        form = AwardAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']
            award = Award(
                name=name,
                year=year,
                           )
            award.save()
            return redirect('awards')
    else:
        form = AwardAddForm()
    return render(request, 'add_award.html', {'form': form})


def edit_film(request, id):
    film = Film.objects.get(id=id)
    if request.method == "POST":
        form = FilmAddForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            director = form.cleaned_data['director']
            actors = form.cleaned_data['actors']
            studio = form.cleaned_data['studio']
            release_date = form.cleaned_data['release_date']
            if not form.cleaned_data['awards']:
                awards = ''
            else:
                awards = form.cleaned_data['awards']
            description = form.cleaned_data['description']
            trailer = form.cleaned_data['trailer']

            if form.cleaned_data['image']:
                film.image = form.cleaned_data['image']

            film.title = title
            film.director = director
            film.studio = studio
            film.release_date = release_date
            film.description = description
            film.trailer = trailer
            film.awards.set(awards)
            film.actors.set(actors)
            film.save()
            return redirect('film', id=id)
    else:
        form = FilmAddForm(instance=film)

    return render(request, 'edit_film.html', {'form': form})


def edit_actor(request):
    return None


def edit_director(request, id):
    director = Director.objects.get(id=id)
    if request.method == "POST":
        form = DirectorAddForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            birthdate = form.cleaned_data['birthdate']
            nationality = form.cleaned_data['nationality']
            if not form.cleaned_data['awards']:
                awards = ''
            else:
                awards = form.cleaned_data['awards']

            if form.cleaned_data['image']:
                director.image = form.cleaned_data['image']

            director.name = name
            director.birthdate = birthdate
            director.nationality = nationality
            director.awards.set(awards)
            director.save()
            return redirect('director', id=id)
    else:
        form = DirectorAddForm(instance=director)

    return render(request, 'edit_film.html', {'form': form})


def edit_studio(request):
    return None


def edit_award(request):
    return None


def delete_film(request):
    return None


def delete_actor(request):
    return None


def delete_director(request):
    return None


def delete_studio(request):
    return None


def delete_award(request):
    return None


def films(request):
    grades_avg = []
    reviews_number = []
    data = []
    films = Film.objects.annotate(avg_grade=Avg('grade__grade')).order_by('-avg_grade')

    for film in films:
        avg = Grade.objects.filter(film__id=film.id).aggregate(Avg('grade'))['grade__avg']
        if avg is None:
            avg = 0
        avg = round(avg, 2)
        grades_avg.append(avg)

        reviews = Review.objects.filter(film__id=film.id).aggregate(Count('review'))['review__count']
        reviews_number.append(reviews)

        data.append((film, avg, reviews))

    print(films)
    print(grades_avg)
    print(reviews_number)

    return render(request, 'films.html', {'data': data})


def register(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'sign_in.html')
    else:
        form = CreateAccountForm()
    return render(request, 'create_account.html', {'form': form})


def director(request, id):
    return None


def review(request, id):
    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            film = Film.objects.get(id=id)
            review = form.cleaned_data['review']

            review = Review(film=film, review=review, user=request.user)
            review.save()

        return redirect('film', id=id)


def grade(request, id):
    if request.method == 'POST':

        form = GradeForm(request.POST)

        if form.is_valid():
            film = Film.objects.get(id=id)
            grade = form.cleaned_data['grade']

            grade = Grade(film=film, grade=grade, user=request.user)
            grade.save()

        return redirect('film', id=id)


def search(request):
    if 'query' in request.POST:
            query = request.POST['query']

            films = Film.objects.filter(title__icontains=query)
            actors = Actor.objects.filter(name__icontains=query)
            directors = Director.objects.filter(name__icontains=query)

            return render(request, 'results.html', {'films': films, 'actors': actors, 'directors': directors, 'query': query})

