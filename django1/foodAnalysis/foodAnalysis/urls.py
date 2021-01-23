from django.urls import path

from . import views

app_name = 'foodAnalysis'
urlpatterns = [
    path('', views.data, name='foodAnalysis')
]
