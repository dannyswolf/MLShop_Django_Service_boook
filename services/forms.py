
from .models import Services
from django import forms
from machines.models import Machines
from service_data.models import ServiceData
from datetime import datetime


class CreateServiceFromMachineForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

    Σκοπός_data = sorted(set(ServiceData.objects.values_list('Σκοπός', flat=True)))
    Ενέργειες_data = sorted(set(ServiceData.objects.values_list('Ενέργειες', flat=True)))
    Σκοπός_choices = [(item, item) for item in Σκοπός_data]
    Ενέργειες_choices = [(item, item) for item in Ενέργειες_data]

    Ημερομηνία = forms.CharField(help_text='Ημερομηνία ολοκλήρωσής εργασίας', required=True,
                                 widget=forms.TextInput(attrs={'type': 'date'}))

    Σκοπός_Επίσκεψης = forms.ChoiceField(choices=Σκοπός_choices, required=False)
    Ενέργειες = forms.ChoiceField(choices=Ενέργειες_choices, required=False)
    Τεχνικός = forms.CharField(max_length=200)
    Μετρητής = forms.CharField(required=False, max_length=12)
    Επ_Service = forms.CharField(required=False, max_length=12)
    Copier_ID = forms.ModelChoiceField(queryset=Machines.objects.all(),
                                       help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')
    ΔΤΕ = forms.CharField(required=False, max_length=100)
    Price = forms.CharField(required=False, max_length=100)
    Σημειώσεις = forms.CharField(widget=forms.Textarea, required=False)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),
                           max_length=100, allow_empty_file=True, required=False)

    def clean_Ημερομηνία(self):
        Ημερομηνία = self.cleaned_data.get('Ημερομηνία')
        # datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
        try:
            new_date = datetime.strptime(Ημερομηνία, '%Y-%m-%d').strftime('%d/%m/%Y')
            return str(new_date)
        except ValueError as error:
            print("----ValueError at Ημερομηνία --- ", __name__, error)
        return Ημερομηνία
