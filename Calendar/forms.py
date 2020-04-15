from .models import Calendar
from django import forms
from service_data.models import ServiceData
from datetime import date, datetime


class CreateCalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ('Ημερομηνία', "Πελάτης", "Τηλέφωνο", "Customer_ID", "Μηχάνημα",
                  "Copier_ID", "Σκοπός", "Ενέργειες", "Τεχνικός", "Επείγων",
                  "Μετρητής", "Επ_Service", "ΔΤΕ", "Price", "Service_ID",
                  "Σημειώσεις", "Ημ_Ολοκλ", "Κατάσταση")

    Σκοπός_data = sorted(set(ServiceData.objects.values_list('Σκοπός', flat=True)))
    Ενέργειες_data = sorted(set(ServiceData.objects.values_list('Ενέργειες', flat=True)))
    Σκοπός_choices = [(item, item) for item in Σκοπός_data]
    Ενέργειες_choices = [(item, item) for item in Ενέργειες_data]

    # Δεν γράφει την ημερομηνία σαν d/m/Y αλλά σαν Y/m/d την αλλάζω στο clean_Ημερομηνία
    Ημερομηνία = forms.CharField(help_text='Ημερομηνία εκτέλεσης εργασίας', required=False,
                                 widget=forms.TextInput(attrs={'type': 'date',
                                                               "value": date.today().strftime("%Y-%m-%d")}))

    Πελάτης = forms.CharField(max_length=200, required=True)
    Τηλέφωνο = forms.CharField(max_length=100, required=False)
    # Customer_ID = forms.IntegerField(required=True)
    Μηχάνημα = forms.CharField(max_length=200, required=True)
    # Copier_ID = forms.IntegerField(required=True)
    Σκοπός = forms.ChoiceField(choices=Σκοπός_choices, required=False)
    Ενέργειες = forms.ChoiceField(choices=Ενέργειες_choices, required=False)
    Μετρητής = forms.CharField(max_length=11, required=False)
    Επ_Service = forms.CharField(max_length=11, required=False)

    Service_ID = forms.IntegerField(required=False, help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')
    Σημειώσεις = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 15}), required=False, max_length=5000)
    Ημ_Ολοκλ = forms.CharField(help_text='Ημερομηνία ολοκλήρωσης εργασίας', required=False,
                               widget=forms.TextInput(attrs={'type': 'date',
                                                             "value": date.today().strftime("%Y-%m-%d")}))
    Κατάσταση = forms.BooleanField(required=False, initial=True,
                                   help_text="<font color='red'><strong>Ενεργό αν δεν έχει τελειώσει η "
                                             "εργασία</strong></font>")

    def clean_Ημερομηνία(self):
        Ημερομηνία = self.cleaned_data.get('Ημερομηνία')
        # datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
        new_date = datetime.strptime(Ημερομηνία, '%Y-%m-%d').strftime('%d/%m/%Y')
        return str(new_date)


class EditCalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ('Ημερομηνία', 'Πελάτης', "Τηλέφωνο",
                  "Copier_ID", "Σκοπός", "Ενέργειες", "Τεχνικός", "Επείγων",
                  "Μετρητής", "Επ_Service", "ΔΤΕ", "Price", "Service_ID",
                  "Σημειώσεις", "Ημ_Ολοκλ", "Κατάσταση")

    Σκοπός_data = sorted(set(ServiceData.objects.values_list('Σκοπός', flat=True)))
    Ενέργειες_data = sorted(set(ServiceData.objects.values_list('Ενέργειες', flat=True)))
    Σκοπός_choices = [(item, item) for item in Σκοπός_data]
    Ενέργειες_choices = [(item, item) for item in Ενέργειες_data]
    # Σκοπός = forms.ChoiceField(Σκοπός_choices,   required=False, widget=forms.Select())
    # Ενέργειες = forms.ChoiceField(Ενέργειες_choices,   required=False, widget=forms.Select())
    # Ημερομηνία = forms.CharField(help_text='Ημερομηνία ολοκλήρωσης εργασίας', required=False,)

    Ημερομηνία = forms.CharField(help_text='Ημερομηνία εκτέλεσης εργασίας', required=True,
                                 widget=forms.TextInput(attrs={'type': 'date'}))

    Πελάτης = forms.CharField(max_length=200, required=True)
    Τηλέφωνο = forms.CharField(max_length=100, required=False)
    # Customer_ID = forms.IntegerField(required=True)
    # Μηχάνημα = forms.CharField(max_length=200, required=True)
    # Copier_ID = forms.IntegerField(required=True)
    Σκοπός = forms.ChoiceField(choices=Σκοπός_choices, required=False)
    Ενέργειες = forms.ChoiceField(choices=Ενέργειες_choices, required=False)

    Μετρητής = forms.CharField(max_length=11, required=False)
    Επ_Service = forms.CharField(max_length=11, required=False)

    Service_ID = forms.IntegerField(required=False, help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')
    Σημειώσεις = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 18}), required=False, max_length=5000)
    Ημ_Ολοκλ = forms.CharField(help_text='Ημερομηνία ολοκλήρωσης εργασίας', required=False,
                               widget=forms.TextInput(attrs={'type': 'date'}))
    Κατάσταση = forms.BooleanField(required=False, initial=True,
                                   help_text="<font color='red'><strong>Ενεργό αν δεν έχει τελειώσει η εργασία</strong></font>")

    def clean_Ημερομηνία(self):
        Ημερομηνία = self.cleaned_data.get('Ημερομηνία')
        # datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
        new_date = datetime.strptime(Ημερομηνία, '%Y-%m-%d').strftime('%d/%m/%Y')
        return str(new_date)

    def clean_Ημ_Ολοκλ(self):
        Ημ_Ολοκλ = self.cleaned_data.get('Ημ_Ολοκλ')
        # datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
        try:
            new_date = datetime.strptime(Ημ_Ολοκλ, '%Y-%m-%d').strftime('%d/%m/%Y')
            return str(new_date)
        except ValueError as error:
            print("----ValueError at Ημ_Ολοκλ ", __name__, error)
        return Ημ_Ολοκλ
