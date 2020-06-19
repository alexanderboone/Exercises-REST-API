from .models import Exercise, MuscleGroup
from rest_framework import serializers

class MuscleGroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MuscleGroup
        fields = ['name']

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    musclegroups = MuscleGroupSerializer(read_only=True, many=True)

    class Meta:
        model = Exercise
        fields = ['name', 'musclegroups', 'mechanics', 'push_pull_legs', 'description']

