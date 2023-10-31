from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import reverse_lazy

app_name = 'ads'
urlpatterns = [
    # path('', views.MainView.as_view(), name='all'),
    # path('main/create/', views.AdCreate.as_view(), name='ad_create'),
    # path('main/<int:pk>/update/', views.AdUpdate.as_view(), name='ad_update'),
    # path('main/<int:pk>/delete/', views.AdDelete.as_view(), name='ad_delete'),
    path('', views.AdListView.as_view(), name='all'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create',
        views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),
    path('ad/<int:pk>/update',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_update'),
    path('ad/<int:pk>/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_delete'),

]

# Note that make_ and ad_ give us uniqueness within this application