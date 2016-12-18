from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Facility


def index(request):
    """Place holder.  probably where the main map page will go"""
    return HttpResponse('Hello from maps index')

def show_facility(request, facility_id):
    """ Facility detail page"""
    loc = get_object_or_404(Facility, pk=facility_id)
    # render(facility_template, loc)
    return render(request, 'maps/show_facility.html', {'facility': loc})

def new_facility(request):
    """new facility page and logic"""
    if request.POST:
        loc = Facility()
        loc.address = request.POST['address']
        loc.country = request.POST['country']
        loc.name = request.POST['name']
        loc.save()
        return HttpResponseRedirect(reverse('facility', args=(loc.pk,)))

    return render(request, 'maps/new.html')
