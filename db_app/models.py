from django.db import models

stepType = (
    ('1', 'on demand'),
    ('2', 'moving'),
    ('3', 'resting'),
)

class elevatorModel(models.Model):
    demand = models.CharField(max_length=200)
    restingFloor = models.CharField(max_length=200, default=0)
    vacancy = models.BooleanField(default=True)
    moving = models.BooleanField(default=True)
    elevatorStep = models.CharField(max_length=200, choices=stepType)

    updated = models.DateTimeField(auto_now=True) #takes a snapshot everytime the field is updated
    created = models.DateTimeField(auto_now_add=True) #takes a snapshot when the table is created

    def __str__(self):
        return self.demand