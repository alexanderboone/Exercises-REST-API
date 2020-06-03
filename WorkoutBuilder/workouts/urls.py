from django.urls import path

from . import views

# Used in reversing urls, e.g. 'app_name:route' as first reverse() arg.
app_name='workouts'

urlpatterns = [
    path('', views.home_view, name='home_view'),

    path('exercises/', views.exercise_list_view, name='exercise-list-view'),
    path('exercises/create/', views.exercise_create_view, name='exercise-create-view'),
    path('exercises/<str:exercise_name>/', views.exercise_detail_view, name='exercise-detail-view'),

    path('workouts/', views.workout_list_view, name='workout-list-view'),
]