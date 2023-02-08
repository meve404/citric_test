from django.forms import ModelForm
from .models import elevatorModel

class elevatorForm(ModelForm):
    class Meta:
        model = elevatorModel
        fields = ['demand']

class updateElevatorForm(ModelForm):
    class Meta:
        model = elevatorModel
        fields = '__all__'