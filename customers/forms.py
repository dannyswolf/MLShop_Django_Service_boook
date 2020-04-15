from django.forms import ModelForm
from .models import Customer


class CustomerForm(ModelForm):

    # Set the fields attribute to the special value '__all__' to indicate that all fields in the model should be used
    class Meta:
        model = Customer
        fields = '__all__'

    # def clean_Τηλέφωνο(self, *args, **kwargs):
    #     """
    #     Ελεγχος ανα υπάρχει το Τηλέφωνο και επιστρέφει το ονομα δλδ Επωνυμία_Επιχείρησης
    #     docs ==> https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet.exists
    #   """
    #     Τηλέφωνο = self.cleaned_data.get("Τηλέφωνο")
    #     if len(str(Τηλέφωνο).replace(" ", "")) != 10 and Τηλέφωνο is not None and Τηλέφωνο is not "":
    #         raise forms.ValidationError("Παρακαλώ 10 ψηφία")
    #     elif Τηλέφωνο is None or Τηλέφωνο is "":
    #         return Τηλέφωνο
    #     else:
    #         if Customer.objects.filter(Τηλέφωνο=Τηλέφωνο).exists():
    #             try:
    #                 customer = Customer.objects.get(Τηλέφωνο=Τηλέφωνο)
    #                 raise forms.ValidationError(f"Id {customer.id} {customer}")
    #             except Customer.MultipleObjectsReturned:
    #                 raise forms.ValidationError("Υπάρχει πολλές φορές")
    #         elif Τηλέφωνο.isdigit():
    #             return Τηλέφωνο
    #         else:
    #             raise forms.ValidationError("Παρακαλώ μόνο αριθμούς")
    #
    #
    # def clean_Κινητό(self, *args, **kwargs):
    #     """
    #     Ελεγχος ανα υπάρχει το Κινητό και επιστρέφει το ονομα δλδ Επωνυμία_Επιχείρησης
    #     docs ==> https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet.exists
    #     """
    #     Κινητό = self.cleaned_data.get("Κινητό")
    #
    #     if len(str(Κινητό).replace(" ", "")) != 10 and Κινητό is not None and Κινητό is not "":
    #         raise forms.ValidationError("Παρακαλώ 10 ψηφία")
    #     elif Κινητό is None or Κινητό is "":
    #         return Κινητό
    #     else:
    #         # customer = Customer.objects.get(Κινητό=Κινητό)
    #         if Customer.objects.filter(Κινητό=Κινητό).exists():
    #             try:
    #                 customer = Customer.objects.get(Κινητό=Κινητό)
    #
    #                 raise forms.ValidationError(f"{customer.id} {customer}")
    #             except Customer.MultipleObjectsReturned:
    #                 raise forms.ValidationError(f"Υπάρχει πολλές φορές")
    #         elif Κινητό.isdigit():
    #             return Κινητό
    #         else:
    #             raise forms.ValidationError("Παρακαλώ μόνο αριθμούς")

    # def clean_Επωνυμία_Επιχείρησης(self, *args, **kwargs):
    #     Επωνυμία_Επιχείρησης = self.cleaned_data.get("Επωνυμία_Επιχείρησης")
    #
    #     if Επωνυμία_Επιχείρησης == None or Επωνυμία_Επιχείρησης == "":
    #         raise forms.ValidationError("Απαραίτητο πεδίο")
    #     elif Customer.objects.filter(Επωνυμία_Επιχείρησης=Επωνυμία_Επιχείρησης).exists():
    #         try:
    #             customer = Customer.objects.get(Επωνυμία_Επιχείρησης=Επωνυμία_Επιχείρησης)
    #             if Επωνυμία_Επιχείρησης == customer:
    #                 return Επωνυμία_Επιχείρησης
    #         except Customer.MultipleObjectsReturned:
    #             raise forms.ValidationError('Υπάρχει')
    #     else:
    #         return Επωνυμία_Επιχείρησης

