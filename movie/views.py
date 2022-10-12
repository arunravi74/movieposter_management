from django.forms import ValidationError
from django.shortcuts import HttpResponse, render,redirect
from django.contrib.auth.models import User
from movie.forms import MoviePosterForm, UpdateUserForm, user_registration_form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from movie.models import Movie

def index(request):
    return render(request,"movie/index.html")

def sign_up(request):
    if request.method == "POST":
        form = user_registration_form(request.POST)
        if form.is_valid():            
            form.save()          
        return redirect("/login")
    else:
        form = user_registration_form
    return render(request,"movie/registration.html",{"form":form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'movie/profile.html', {'user_form': user_form})

@login_required
def dashboard(request):
    movie = Movie.objects.filter(users=request.user)
    return render(request,"movie/dashboard.html",{"movie":movie,"media_url":settings.MEDIA_URL})

@login_required
def image_upload(request):
    if request.method == 'POST':
        form = MoviePosterForm(request.POST, request.FILES)
        if form.is_valid():
            movie = Movie.objects.create(movie_name=form.cleaned_data["movie_name"],movie_poster=form.cleaned_data["movie_poster"],
            movie_description=form.cleaned_data["movie_description"])
            movie.save()
            return redirect('dashboard')
        else:
            return render(request,"movie/poster.html",{"form":form})            
    else:
        form = MoviePosterForm()
    return render(request,"movie/poster.html",{"form":form})
