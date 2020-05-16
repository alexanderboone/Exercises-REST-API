# Generated by Django 3.0.6 on 2020-05-16 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_exercise_mechanics'),
    ]

    operations = [
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='muscle_group',
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscle_group',
            field=models.ManyToManyField(to='workouts.MuscleGroup'),
        ),
    ]
