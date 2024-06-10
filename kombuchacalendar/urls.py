from django.urls import path
from . import views

app_name = 'kombuchacalendar'
urlpatterns = [
    path('', views.index, name='index'),
    path('brew_batch/', views.brew_batch, name='brew_batch')
]
