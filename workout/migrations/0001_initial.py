# Generated by Django 4.2.11 on 2024-03-27 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('reps', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('excercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workout.excercise')),
            ],
        ),
    ]
