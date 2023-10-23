from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from movies.models import Movie, Genre
from movies.forms import MakeForm


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Genre.objects.count()
        al = Movie.objects.all()

        ctx = {'genre_count': mc, 'movie_list': al}
        return render(request, 'movies/movie_list.html', ctx)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Genre.objects.all()
        ctx = {'genre_list': ml}
        return render(request, 'movies/genre_list.html', ctx)

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('movies:all')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('movies:all')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('movies:all')


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:all')

# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References



# https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#createview