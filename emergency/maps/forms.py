from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Facility

class FacilityForm(ModelForm):
    """ Form for creating new Facilities. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'facility-form-id'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'new'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-9'

        self.helper.add_input(Submit('submit', 'Submit'))


    class Meta:
        model = Facility
        exclude = ['lat', 'long', 'id', 'created_at', 'updated_at']
