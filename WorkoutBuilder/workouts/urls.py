from django.urls import path, include
from rest_framework import routers
from . import views

# Router uses for API
router = routers.DefaultRouter()
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'musclegroups', views.MuscleGroupViewSet)

# Used in reversing urls, e.g. 'app_name:route' as first reverse() arg.
#app_name='workouts'

urlpatterns = [
    path('', views.home_view, name='home_view'),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('exercises/', views.exercise_list_view, name='exercise-list-view'),
    path('exercises/create/', views.exercise_create_view, name='exercise-create-view'),
    path('exercises/<str:exercise_name>/', views.exercise_detail_view, name='exercise-detail-view'),
]