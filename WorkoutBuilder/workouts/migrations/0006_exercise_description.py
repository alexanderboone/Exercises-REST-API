# Generated by Django 3.0.6 on 2020-05-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_exercise_muscle_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
