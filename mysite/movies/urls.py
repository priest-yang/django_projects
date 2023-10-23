from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/4.2/topics/http/urls/
app_name = 'movies'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.AutoCreate.as_view(), name='movie_create'),
    path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='movie_update'),
    path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='movie_delete'),
    path('lookup/', views.MakeView.as_view(), name='genre_list'),
    path('lookup/create/', views.MakeCreate.as_view(), name='genre_create'),
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='genre_update'),
    path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='genre_delete'),
]