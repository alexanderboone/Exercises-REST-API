from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),

    path('exercises/', views.exercise_list_view, name='exercise_list_view'),
    path('exercises/create/', views.exercise_create_view, name='exercise_create_view'),
    path('exercises/<str:exercise_name>/', views.exercise_detail_view, name='exercise_detail_view'),

    path('workouts/', views.workout_list_view, name='workout_list_view'),
]