from django.forms import ModelForm

from .models import Facility

from mapwidgets import GooglePointFieldWidget

class FacilityForm(ModelForm):
    """ Form for creating new Facilities. """

    class Meta:
        model = Facility
        # fields = ['name', 'address', 'country', 'services']
        widgets = dict(coordinates=GooglePointFieldWidget)
        exclude = ['created_at', 'updated_at']
