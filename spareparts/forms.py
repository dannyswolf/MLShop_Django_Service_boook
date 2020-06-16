
from .models import SpareParts
from django import forms
from services.models import Services
from customers.models import Customer

class AddSparePartsToService(forms.ModelForm):
    # PARTS_NR = forms.CharField(max_length=50)
    # ΠΕΡΙΓΡΑΦΗ = forms.CharField(widget=forms.Textarea, required=False)
    # ΚΩΔΙΚΟΣ = forms.CharField(max_length=10, required=False)
    # ΤΕΜΑΧΙΑ = forms.CharField(max_length=100, required=False)
    # ΠΑΡΑΤΗΡΗΣΗΣ = forms.CharField(widget=forms.Textarea, required=False)
    # Customer_ID = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True)
    # ΜΗΧΑΝΗΜΑ = forms.CharField(max_length=100, required=False)
    # Service_ID = forms.IntegerField()
    # Calendar_ID = forms.IntegerField()

    class Meta:
        model = SpareParts
        fields = '__all__'

        
