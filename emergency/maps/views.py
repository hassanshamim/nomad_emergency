from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Location


def index(request):
    """Place holder.  probably where the main map page will go"""
    return HttpResponse('Hello from maps index')

def show_location(request, location_id):
    """ Location detail page"""
    loc = get_object_or_404(Location, pk=location_id)
    # render(location_template, loc)
    return render(request, 'maps/show_location.html', {'location': loc})

def new_location(request):
    """new location page and logic"""
    if request.POST:
        loc = Location()
        loc.address = request.POST['address']
        loc.country = request.POST['country']
        loc.name = request.POST['name']
        loc.save()
        return HttpResponseRedirect(reverse('location', args=(loc.pk,)))

    return render(request, 'maps/new.html')
