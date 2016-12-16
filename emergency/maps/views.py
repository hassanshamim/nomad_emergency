from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Location


def index(request):
    return HttpResponse('Hello from maps index')

def show_location(request, location_id):
    loc = get_object_or_404(Location, pk=location_id)
    # render(location_template, loc)
    return render(request, 'maps/show_location.html', {'location': loc})
