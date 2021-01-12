from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('year/<str:branch>/', views.year , name='year'),
    path('department/<int:year>/<str:branch>/', views.department, name='department'),
    path('subjects/<str:branch>/<int:year>/<str:mod>/', views.subjects, name='subjects'),
    path('multi/<str:mod>/<str:subject>/', views.multi, name='multi'),
    path('firstyear/<str:branch>/', views.firstyear, name='firstyear'),
]