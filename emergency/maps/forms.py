from django.forms import ModelForm

from .models import Facility

class FacilityForm(ModelForm):
    """ Form for creating new Facilities. """
    class Meta:
        model = Facility
        fields = ['name', 'address', 'country', 'services']
