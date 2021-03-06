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
    musclegroups = models.ManyToManyField(MuscleGroup)
    mechanics = models.CharField(
        max_length=4,
        choices=mechanics_choices,
        default='NA'
    )
    push_pull_legs = models.CharField(
        max_length=4,
        choices=ppl_choices,
        default='NA'
    )
    description = models.TextField(default='')

    def get_absolute_url(self):
        '''Return the url of the exercise detail view page'''
        return reverse("exercise-detail-view", kwargs={"exercise_name": self.name.replace(' ', '-').lower()})

    def __str__(self):
        return self.name