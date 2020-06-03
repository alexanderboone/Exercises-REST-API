from django.db import models
from django.urls import reverse

mechanics_choices = [
    ('Comp', 'Compound'),
    ('Iso', 'Isolation'),
    ('NA', 'Not Applicable')
]

ppl_choices = [
    ('Push', 'Push'),
    ('Pull', 'Pull'),
    ('Legs', 'Legs')
]

class MuscleGroup(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=64)
    muscle_group = models.ManyToManyField('MuscleGroup', related_name='exercises')
    mechanics = models.CharField(
        max_length=4,
        choices=mechanics_choices,
        default='NA'
    )
    ppl = models.CharField(
        max_length=4,
        choices=ppl_choices,
        default='NA'
    )
    description = models.TextField(default='')

    def get_absolute_url(self):
        '''Return the url of the exercise detail view page'''
        return reverse("workouts:exercise-detail-view", kwargs={"exercise_name": self.name.replace(' ', '-').lower()})

    def __str__(self):
        return self.name