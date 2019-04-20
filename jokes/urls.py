from django.urls import path

from . import views

app_name = 'jokes'
urlpatterns = [
    path('', views.index, name='index'),
    path('jokes/', views.jokes, name='jokes')
]
