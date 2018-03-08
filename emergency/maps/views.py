from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Facility
from .forms import FacilityForm


def index(request):
    """Place holder.  probably where the main map page will go"""
    return render(request, 'maps/index.html')

def show_facility(request, facility_id):
    """ Facility detail page"""
    loc = get_object_or_404(Facility, pk=facility_id)
    # render(facility_template, loc)
    return render(request, 'maps/show_facility.html', {'facility': loc})

def new_facility(request):
    """new facility page and logic"""
    if request.method == 'POST':
        form = FacilityForm(request.POST)

        if form.is_valid():
            fac = form.save()

            return HttpResponseRedirect(reverse('facility', args=(fac.pk,)))

    else:
        form = FacilityForm()


    return render(request, 'maps/new.html', context={'facility_form': form})
