from django.urls import path
from . import views

app_name = 'kombuchacalendar'
urlpatterns = [
    path('', views.index, name='index'),
    path('brew_batch/', views.brew_batch, name='brew_batch'),
    path('batches/', views.BatchListView.as_view(), name='batches'),
    path('batch/<int:pk>/', views.BatchDetailView.as_view(), name='batch_detail'),
    path('batch_update/<int:batch_id>/', views.batch_update, name='batch_update')
]
