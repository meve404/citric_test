from rest_framework.serializers import ModelSerializer
from db_app.models import elevatorModel

class elevatorSerial(ModelSerializer):
    class Meta:
        model = elevatorModel
        fields = '__all__'