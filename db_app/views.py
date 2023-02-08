from django.shortcuts import render, redirect
from .forms import elevatorForm, updateElevatorForm
from .models import elevatorModel
from django.shortcuts import get_object_or_404
from django.contrib import messages
import requests
from django.http import HttpResponse

def elevator(request):
    #----- Gets the data directly from de db -----#
    all_demands = elevatorModel.objects.all().order_by('created')

    #----- Works with the form and its logic
    elevator_form = elevatorForm(request.POST or None)

    if request.method == 'POST' and elevator_form.is_valid():
        uncommited_form_elevetor = elevator_form.save(commit=False) #to define manually the required fields

        entered_demand = elevator_form.cleaned_data.get('demand') # gets the demand typed by user

        try: # When db does not have entries, the elevator is has no resting floor yet
            last_entry_resting_floor = all_demands.last().restingFloor # gets where the elevator currently is
        except:
            last_entry_resting_floor = 0

        if entered_demand == last_entry_resting_floor: # If the elevator is already on last floor, it warnings the user
            messages.warning(request, f'The elevator is already on floor {entered_demand}')
        else:
            uncommited_form_elevetor.elevatorStep = 'on demand'
            uncommited_form_elevetor.moving = False
            elevator_form.save()
            return redirect(f'elevator-moving', entered_demand) # Redirects to moving step

    context = {'elevator_form':elevator_form, 'all_demands':all_demands}
    return render(request, 'db_app/elevator.html', context)

#----- Moving Step -----#
def moving_elevator(request, lastDemand):
    new_elevator_entry = elevatorModel(demand=lastDemand, vacancy=False, elevatorStep='moving') # Creates a new entry with step moving
    new_elevator_entry.save()
    return redirect(f'resting-elevator', lastDemand)

#----- Resting Step -----#
def resting_elevator(request, lastDemand):
    new_elevator_entry = elevatorModel(demand=0, restingFloor=lastDemand, moving=False, elevatorStep='resting')  # Creates a new entry with step resting
    new_elevator_entry.save()
    return redirect(f'elevator')

#----- Delete Demand -----#
def del_elevator(request, id):
    demand = get_object_or_404(elevatorModel, pk=id)
    demand.delete()
    return redirect('elevator')

#----- Update Demand -----#
def update_elevator(request, id):
    demand = get_object_or_404(elevatorModel, pk=id)
    elevator_form = updateElevatorForm(request.POST or None, instance=demand)

    if request.method == 'POST' and elevator_form.is_valid():
        elevator_form.save()
        return redirect('elevator')

    context = {'elevator_form':elevator_form}
    return render(request, 'db_app/elevator.html', context)

def demands_json(request):
    #----- Gets the data from API in json format -----#
    get_demands = requests.get(f'http://localhost:8000/elevator-api/get-demands') #gets the demands
    demands_data = get_demands.json() #translates the demands data

    context = {'demands_data':demands_data}
    return render(request, 'db_app/elevator.html', context)