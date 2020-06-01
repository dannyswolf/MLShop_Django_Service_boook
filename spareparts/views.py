from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.forms.models import modelform_factory
from django.forms import Textarea
from .forms import AddSparePartsToService
from django.http import JsonResponse


import json

from .models import SpareParts
from machines.models import Machines
from services.models import Services
from customers.models import Customer

from warehouse.models import (A_ΟΡΟΦΟΣ, BROTHER, CANON, KONICA, KYOCERA, LEXMARK, OKI, RICOH, SAMSUNG, SHARP,
                                ΜΕΛΑΝΑΚΙΑ, ΜΕΛΑΝΟΤΑΙΝΙΕΣ, ΤΟΝΕΡ, ΦΩΤΟΤΥΠΙΚΑ)


# Create your views here.
class SparePartsListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    # model = SpareParts
    template_name = 'spareparts/spareparts_detail.html'
    # sorted(data_from_calendar, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y"))
    # queryset = sorted(Services.objects.all(), key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"))
    # sort(key=lambda date: datetime.strptime(date, '"%d/%m/%Y"))
    queryset = SpareParts.objects.prefetch_related('Service_ID').prefetch_related('Customer_ID')
    # select_related('Customer_ID').prefetch_related('Service_ID__Copier_ID')
    fields = '__all__'
    # form_class = CustomerForm
    # paginate_by = 5


# class SparePartsCreateView(LoginRequiredMixin, CreateView):
#     redirect_field_name = ''
#     model = SpareParts
#     fields = '__all__'
#     template_name = 'spareparts/add_spareparts.html'

#     def get_success_url(self):
#         return reverse_lazy('spareparts:spareparts')
    
#     def form_valid(self, form):
#         print(self.form_valid)
#         print(self.request.POST)




#     # def form_valid(self, form):
#     #     print(self.request)
#     #     print(self.form)
#     #     #data = form.cleaned_data
#     #     # print("data", data)
#     #     return super().form_valid(form)

@login_required()
def SparePartsCreateView(request, *args, **kwargs):
    
    # Javascript 
    if request.is_ajax():
        print("request.POST", request.POST)
        Service_ID =  int(request.POST.get('somedata[Service_ID]'))
        Customer_ID = int(request.POST.get('somedata[Customer_ID]'))
        # neeed Services Instance 
        service_instance = Services.objects.get(pk=Service_ID)
        customer_instance = Customer.objects.get(pk=Customer_ID)

        ΠΕΡΙΓΡΑΦΗ   = request.POST.get('somedata[ΠΕΡΙΓΡΑΦΗ]')
        ΚΩΔΙΚΟΣ     = request.POST.get('somedata[ΚΩΔΙΚΟΣ]')
        Copier_ID   = request.POST.get('somedata[ΜΗΧΑΝΗΜΑ]')
        category    = request.POST.get('somedata[category]')
        Service_ID  = service_instance
        Customer_ID = customer_instance
        ΜΗΧΑΝΗΜΑ = Machines.objects.get(pk=Copier_ID)
        
        # Εισαγωγη νεου ανταλλακτικού ή προσθήκη +1 στο ηδη υπάρχων
        new_obj, created = SpareParts.objects.get_or_create(ΠΕΡΙΓΡΑΦΗ=ΠΕΡΙΓΡΑΦΗ, ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ, 
        ΜΗΧΑΝΗΜΑ=ΜΗΧΑΝΗΜΑ.Εταιρεία, Service_ID=Service_ID, Customer_ID=Customer_ID)
        if created:
            new_obj.ΤΕΜΑΧΙΑ = 1  # Ορίζουμε ενα τεμάχια
            new_obj.save()
            try:
                # Αφαιρεσει -1 απο την αποθήκη
                if category == 'brother':
                    sparepart = BROTHER.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'canon':
                    sparepart = CANON.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'konica':
                    sparepart = KONICA.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'kyocera':
                    sparepart = KYOCERA.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'lexmark':
                    sparepart = LEXMARK.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'oki':
                    sparepart = OKI.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'ricoh':
                    sparepart = RICOH.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'samsung':
                    sparepart = SAMSUNG.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'sharp':
                    sparepart = SHARP.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'melanakia':
                    sparepart = ΜΕΛΑΝΑΚΙΑ.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'melanotainies':
                    sparepart = ΜΕΛΑΝΟΤΑΙΝΙΕΣ.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'toner':
                    sparepart = ΤΟΝΕΡ.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'fototypika':
                    sparepart = ΦΩΤΟΤΥΠΙΚΑ.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
            except MultipleObjectsReturned:
                json_response = { 
                                'id': new_obj.pk,
                                "ΠΕΡΙΓΡΑΦΗ": new_obj.ΠΕΡΙΓΡΑΦΗ,
                                "ΚΩΔΙΚΟΣ": new_obj.ΚΩΔΙΚΟΣ,
                                'status': 202
                                } 
                return JsonResponse(json_response)

            sparepart.ΤΕΜΑΧΙΑ = int(sparepart.ΤΕΜΑΧΙΑ) -1
            sparepart.save()
            json_response = { 
                                'id': new_obj.pk,
                                "ΠΕΡΙΓΡΑΦΗ": new_obj.ΠΕΡΙΓΡΑΦΗ,
                                "ΚΩΔΙΚΟΣ": new_obj.ΚΩΔΙΚΟΣ,
                                'status': 201
            } 
            return JsonResponse(json_response)
        else:   # προσθήκη +1 στο ηδη υπάρχων
            new_obj.ΤΕΜΑΧΙΑ = int(new_obj.ΤΕΜΑΧΙΑ) + 1
            new_obj.save()
            try:
                # Αφαιρεσει -1 απο την αποθήκη
                if category == 'brother':
                    sparepart = BROTHER.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'canon':
                    sparepart = CANON.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'konica':
                    sparepart = KONICA.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'kyocera':
                    sparepart = KYOCERA.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'lexmark':
                    sparepart = LEXMARK.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'oki':
                    sparepart = OKI.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'ricoh':
                    sparepart = RICOH.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'samsung':
                    sparepart = SAMSUNG.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'sharp':
                    sparepart = SHARP.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'melanakia':
                    sparepart = ΜΕΛΑΝΑΚΙΑ.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'melanotainies':
                    sparepart = ΜΕΛΑΝΟΤΑΙΝΙΕΣ.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'toner':
                    sparepart = ΤΟΝΕΡ.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)
                elif category == 'fototypika':
                    sparepart = ΦΩΤΟΤΥΠΙΚΑ.objects.get(ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ)

            except MultipleObjectsReturned:
                json_response = { 
                                'id': new_obj.pk,
                                "ΠΕΡΙΓΡΑΦΗ": new_obj.ΠΕΡΙΓΡΑΦΗ,
                                "ΚΩΔΙΚΟΣ": new_obj.ΚΩΔΙΚΟΣ,
                                'status': 202
                                } 
                return JsonResponse(json_response) 

            sparepart.ΤΕΜΑΧΙΑ = int(sparepart.ΤΕΜΑΧΙΑ) -1
            sparepart.save()
            json_response = { 
                                'id': new_obj.pk,
                                "ΠΕΡΙΓΡΑΦΗ": new_obj.ΠΕΡΙΓΡΑΦΗ,
                                "ΚΩΔΙΚΟΣ": new_obj.ΚΩΔΙΚΟΣ,
                                'status': 200
            } 
            return JsonResponse(json_response)
     
        


    form = AddSparePartsToService
    if request.method == "GET":
        content = {
            "form": form
        }
        return render(request, "spareparts/add_spareparts.html", content)
    # if request.method == "POST":
    #     print("request.POST", request.POST)
    #     Customer_ID = request.POST.get('Customer_ID')
    #     Service_ID = request.POST.get('Service_ID')
    #     ΚΩΔΙΚΟΣ = request.POST.get('ΚΩΔΙΚΟΣ')
    #     ΜΗΧΑΝΗΜΑ = request.POST.get('ΜΗΧΑΝΗΜΑ')
    #     machine = Machines.objects.filter(id=ΜΗΧΑΝΗΜΑ)
    #     ΠΕΡΙΓΡΑΦΗ  = request.POST.get('ΠΕΡΙΓΡΑΦΗ')
    #     print("Customer_ID", Customer_ID)
    #     print("Service_ID", Service_ID)
    #     print("ΚΩΔΙΚΟΣ", ΚΩΔΙΚΟΣ)
    #     print("ΜΗΧΑΝΗΜΑ", ΜΗΧΑΝΗΜΑ)
    #     print("machine", machine)
    #     print("ΠΕΡΙΓΡΑΦΗ", ΠΕΡΙΓΡΑΦΗ)
    #     new_item = SpareParts(ΠΕΡΙΓΡΑΦΗ=ΠΕΡΙΓΡΑΦΗ, ΚΩΔΙΚΟΣ=ΚΩΔΙΚΟΣ, ΤΕΜΑΧΙΑ=1, ΜΗΧΑΝΗΜΑ=machine, 
    #     Service_ID=Service_ID, Customer_ID=Customer_ID)
    #     new_item.save()

    #     return JsonResponse(new_item, status=201)


@login_required()
def search_spareparts_view(request):
    # all_objects = Customer.objects.all()
    paginate_by = 20
    object_list = {}
    # "q" ειναι το ονομα στην φορμα form του αρχείου customer_detail.html ---> <input name="q" ....
    # search_query ==> οτι πληκτρολογεί ο χρήστης για ανναζήτηση στο input με name="q"
    search_query = request.GET.get("q")
    if search_query != "" and search_query is not None:
        # __icontains  Case-insensitive Μη ευαίσθητο σε περίπτωση
        # __contains     Case-sensitive      Ευαίσθητα σε μικροσκοπικά
        # SQLite doesn’t support case-sensitive
        all_objects = SpareParts.objects.filter(
            Q(PARTS_NR__icontains=search_query) |
            Q(ΠΕΡΙΓΡΑΦΗ__icontains=search_query) |
            Q(ΚΩΔΙΚΟΣ__icontains=search_query) |
            Q(ΜΗΧΑΝΗΜΑ__icontains=search_query) |
            Q(Customer_ID__Επωνυμία_Επιχείρησης__icontains=search_query)
        ).order_by('Customer_ID__Επωνυμία_Επιχείρησης')
        # if not all_objects:
        #     all_objects = Customer.objects.all()
        #     return  render(request, "customers/customers_detail.html", {"object": all_objects})
        # το "object_list" ειναι το ´κλειδί' που οριζουμε στα δεδομένα  all_objects για να παρει το αρχείο
        # search_customer_result.html
        paginator = Paginator(all_objects, 5)  # 10 posts per page
        page = request.GET.get('page')
        # if not all_objects:
        #     all_objects = Customer.objects.all()
        #     return  render(request, "customers/customers_detail.html", {"object": all_objects})
        # το "object_list" ειναι το ´κλειδί' που οριζουμε στα δεδομένα  all_objects για να παρει το αρχείο
        # search_customer_result.html
        try:
            all_objects = paginator.page(page)
        except PageNotAnInteger:
            all_objects = paginator.page(1)
        except EmptyPage:
            all_objects = paginator.page(paginator.num_pages)
        object_list = {"object_list": all_objects}
    return render(request, "spareparts/search_spareparts_result.html", object_list)


class EditSparePart(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # services = forms.ModelChoiceField(queryset=Services.objects.all())
    model = SpareParts
    # fields = ['PARTS_NR', 'ΠΕΡΙΓΡΑΦΗ', 'ΚΩΔΙΚΟΣ', 'ΤΕΜΑΧΙΑ', 'ΠΑΡΑΤΗΡΗΣΗΣ', ]
    form_class = modelform_factory(SpareParts,
                                   widgets={
                                       "ΠΑΡΑΤΗΡΗΣΗΣ": Textarea(attrs={'cols': 40, 'rows': 10}),
                                       'ΠΕΡΙΓΡΑΦΗ': Textarea(attrs={'cols': 40, 'rows': 10})

                                   }, fields=('PARTS_NR', 'ΚΩΔΙΚΟΣ', 'ΤΕΜΑΧΙΑ', 'ΠΕΡΙΓΡΑΦΗ',
                                              'ΠΑΡΑΤΗΡΗΣΗΣ'))
    template_name = 'spareparts/detail.html'
    success_url = reverse_lazy('spareparts:spareparts')
    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self):
        id_ = self.kwargs.get("spareparts_id")  # apo to urls.py -->> path('<int:machine_id>'....
        return get_object_or_404(SpareParts, id=id_,)

    def get_context_data(self, **kwargs):
        # id_ = self.kwargs.get("calendar_id")  Δεν χρειάζεται εδώ
        context = super(EditSparePart, self).get_context_data(**kwargs)
        context['context_data'] = self.object  # whatever you would like
        spareparts = context['spareparts']
        ΜΗΧΑΝΗΜΑ = spareparts.ΜΗΧΑΝΗΜΑ
        serial = ΜΗΧΑΝΗΜΑ.split('Σειριακός: ', -1)[-1]
        ΜΗΧΑΝΗΜΑ_queryset = Machines.objects.filter(Serial=serial).values_list('id')  # return a <QuerySet [(357,)]>
        try:
            machine_id = ΜΗΧΑΝΗΜΑ_queryset[0][0]
        except IndexError as error:  # Όταν το μηχάνημα δεν έχει Σειριακό
            machine_id = 2
        context['machine_id'] = machine_id
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class DeleteSparePart(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = SpareParts
    template_name = 'spareparts/confirm_delete.html'
    success_url = reverse_lazy('spareparts:spareparts')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spareparts_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(SpareParts, id=id_)
