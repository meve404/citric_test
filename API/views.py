from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import elevatorSerial
from db_app.models import elevatorModel

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /elevator-api',
        'GET /elevator-api/get-demands'
    ]
    return Response(routes)

@api_view(['GET'])
def get_demands(request):
    all_demands = elevatorModel.objects.all() # Gets all demands from DB
    serial_demands = elevatorSerial(all_demands, many=True) # converts to json format
    return Response(serial_demands.data)