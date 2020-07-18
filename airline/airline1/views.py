from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Flight, Passenger
from django.urls import reverse
# Create your views here.

def index(request):
    context = {
    "airline1": Flight.objects.all()
    }
    return render(request, "airline1/index.html", context)



def flight(request, flight_id):
    try:
        # pk stands for primary key
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise  Http404("Flight does not exist")

    context = {
    "airline1": flight,
    "passengers":flight.passengers.all(),
    "non_passengers": Passenger.objects.exclude(airline1=flight).all()
    }
    return render(request, "airline1/flight.html", context)


def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, "airline1/error.html", {"message": "No selection"})
    except Flight.DoesNotExist:
        return render(request, "airline1/error.html", {"message": "No Flight"})
    except Passenger.DoesNotExist:
        return render(request, "airline1/error.html", {"message": "No Passenger"})


    passenger.airline1.add(flight)
    return HttpResponseRedirect(reverse("flight"))
