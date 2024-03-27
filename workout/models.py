from django.db import models

class Excercise(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class TrainingEvent(models.Model):
    excercise = models.ForeignKey(Excercise, null=True ,on_delete = models.SET_NULL)
    date = models.DateTimeField()
    reps = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.excercise.name} - {str(self.date)}"