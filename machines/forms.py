from customers.models import Customer
from django import forms
from datetime import datetime
from machines.models import Machines


class AddMachineFromCustomersForm(forms.Form):
    class Meta:
        model = Machines
        fields = '__all__'

    # Εταιρεία_data = sorted(set(Companies.objects.values_list('Εταιρεία', flat=True)))
    # Μοντέλο_data = sorted(set(Companies.objects.values_list('Μοντέλο', flat=True)))
    # Εταιρεία_choices = [(item, item) for item in Εταιρεία_data]
    # Μοντέλο_choices =[(item, item) for item in Μοντέλο_data]
    #
    # Εταιρεία = forms.ChoiceField(choices=Εταιρεία_choices, required=False)
    # Μοντέλο = forms.ChoiceField(choices=Μοντέλο_choices, required=False)

    Εταιρεία = forms.CharField(max_length=50)
    Serial = forms.CharField(max_length=30, required=True)
    Εναρξη = forms.CharField(help_text='Ημερομηνία Εναρξης', required=False,
                                        widget=forms.TextInput(attrs={'type': 'date'}))
    Μετρητής_έναρξης = forms.CharField(max_length=200, required=False)
    Πελάτης = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True)
    Σημειώσεις = forms.CharField(widget=forms.Textarea, required=False)
    Κατάσταση = forms.BooleanField(required=True, initial=True, help_text='<font color="red"><b>Ενεργό αν δεν έχει αποσυρθεί το μηχάνημα</b></font>')

    def clean_Εναρξη(self):
        Εναρξη = self.cleaned_data.get('Εναρξη')
        # datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
        try:
            new_date = datetime.strptime(Εναρξη, '%Y-%m-%d').strftime('%d/%m/%Y')
            return str(new_date)
        except ValueError as error:
            print("----ValueError at Εναρξη --- ", __name__, error)
        return Εναρξη


class EditMachineForm(forms.ModelForm):
    class Meta:
        model = Machines
        fields = '__all__'

    # Εταιρεία_data = sorted(set(Companies.objects.values_list('Εταιρεία', flat=True)))
    # Μοντέλο_data = sorted(set(Companies.objects.values_list('Μοντέλο', flat=True)))
    # Εταιρεία_choices = [(item, item) for item in Εταιρεία_data]
    # Μοντέλο_choices =[(item, item) for item in Μοντέλο_data]
    #
    # Εταιρεία = forms.ChoiceField(choices=Εταιρεία_choices, required=False)
    # Μοντέλο = forms.ChoiceField(choices=Μοντέλο_choices, required=False)

    Εταιρεία = forms.CharField(max_length=50)
    Serial = forms.CharField(max_length=30, required=True)
    Εναρξη = forms.CharField(help_text='Ημερομηνία Εναρξης', required=False,
                             widget=forms.TextInput(attrs={'type': 'date'}))
    Μετρητής_έναρξης = forms.CharField(max_length=200, required=False)
    Πελάτης = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True)
    Σημειώσεις = forms.CharField(widget=forms.Textarea, required=False)
    Κατάσταση = forms.BooleanField(required=True, initial=True, help_text='<font color="red"><b>Ενεργό αν δεν έχει αποσυρθεί το μηχάνημα</b></font>')

    def clean_Εναρξη(self):
        Εναρξη = self.cleaned_data.get('Εναρξη')
        # datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
        try:
            new_date = datetime.strptime(Εναρξη, '%Y-%m-%d').strftime('%d/%m/%Y')
            return str(new_date)
        except ValueError as error:
            print("----ValueError at Εναρξη --- ", __name__, error)
        return Εναρξη