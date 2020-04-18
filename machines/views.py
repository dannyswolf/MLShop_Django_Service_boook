from django.shortcuts import render, get_object_or_404
from .models import Machines
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.forms.models import modelform_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
from services.models import Services
from .forms import AddMachineFromCustomersForm, EditMachineForm
from customers.models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Copiers_Log.models import CopiersLog


# Ενεργά μηχανήματα
class MachinesListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    model = Machines
    template_name = 'machines/machines_detail.html'
    queryset = Machines.objects.filter(Κατάσταση=True).order_by('Πελάτης__Επωνυμία_Επιχείρησης')

    fields = '__all__'
    # form_class = CustomerForm
    paginate_by = 7


# Ανενεργά μηχανήματα
class InactiveMachinesListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    model = Machines
    template_name = 'machines/inactive_machines_detail.html'
    queryset = Machines.objects.filter(Κατάσταση=False).order_by('Πελάτης__Επωνυμία_Επιχείρησης')

    fields = '__all__'
    # form_class = CustomerForm
    paginate_by = 7


class CreateMachine(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    form_class = AddMachineFromCustomersForm
    # model = Machines
    # fields = '__all__'
    template_name = 'machines/create.html'

    def get_success_url(self):
        return reverse_lazy('machines:edit_machine', args=(self.object.id,))


class EditMachine(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # services = forms.ModelChoiceField(queryset=Services.objects.all())
    model = Machines
    form_class = EditMachineForm
    template_name = 'machines/detail.html'
    success_url = reverse_lazy('machines:machines')

    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self, ):
        id_ = self.kwargs.get("machine_id")  # apo to urls.py -->> path('<int:machine_id>'....
        return get_object_or_404(Machines, id=id_, )

    def get_initial(self):
        initial = super(EditMachine, self).get_initial()

        try:
            old_date = self.object.Εναρξη
            new_date = datetime.strptime(old_date, '%d/%m/%Y').strftime('%Y-%m-%d')
            initial['Εναρξη'] = new_date
            return initial
        except ValueError as error:
            print("--------ValueError at Εναρξη -----------", __name__, 'Function -- EditMachine --', error)
            return initial

    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("machine_id")
        context = super(EditMachine, self).get_context_data(**kwargs)
        context['services'] = Services.objects.filter(Copier_ID=id_)  # whatever you would like

        dict_services = context['services'].values()
        try:
            sorted_services = sorted(dict_services, key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"),
                                     reverse=False)
            context['services'] = sorted_services
        except ValueError as error:
            print("--ERROR--", error)
            pass
        except TypeError as error:
            print("--ERROR--", error)
            pass
        # context['services'] = sorted_services
        context['machine_id'] = id_
        # customer = Machines.objects.filter(pk=id_).values('Πελάτης',)
        # context['customer'] = Customer.objects.filter(pk=customer[0]['Πελάτης'])
        context['customer'] = Machines.objects.filter(pk=id_)
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class MachineDelete(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = Machines
    template_name = 'machines/confirm_delete.html'
    success_url = reverse_lazy('machines:machines')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("machine_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(Machines, id=id_)


# Αναζήτηση ενεργων
@login_required()
def search_machine_view(request):
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
        all_objects = Machines.objects.filter(Κατάσταση=True).filter(
            Q(Εταιρεία__icontains=search_query) |
            Q(id__icontains=search_query) |
            Q(Serial__icontains=search_query) |
            Q(Πελάτης__Επωνυμία_Επιχείρησης__icontains=search_query) |
            Q(Σημειώσεις__icontains=search_query)
        ).order_by('Πελάτης__Επωνυμία_Επιχείρησης')
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
    return render(request, "machines/search_machine_result.html", object_list)


# Αναζήτηση ανενεργών μηχανημάτων
@login_required()
def search_inactive_machine_view(request):
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
        all_objects = Machines.objects.filter(Κατάσταση=False).filter(
            Q(Εταιρεία__icontains=search_query) |
            Q(id__icontains=search_query) |
            Q(Serial__icontains=search_query) |
            Q(Πελάτης__Επωνυμία_Επιχείρησης__icontains=search_query) |
            Q(Σημειώσεις__icontains=search_query)
        ).order_by('Πελάτης__Επωνυμία_Επιχείρησης')
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
    return render(request, "machines/search_machine_result.html", object_list)


@login_required()
def add_machine_from_customers(request, customer_id, **kwargs):
    customer = Customer.objects.all().filter(pk=customer_id)
    initial_data = {
        'Πελάτης': customer[0]
    }
    success_url = reverse_lazy('machines:edit_machine')
    form = AddMachineFromCustomersForm(request.POST or None, initial=initial_data)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            #  serial χωρίς κενα
            Serial = data['Serial'].replace(" ", "_")

            print("Serial", Serial)
            form.instance.Serial = Serial
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'machines/add_machine_to_customer.html', context)


# Μεταφορά μηχανήματος
class TransferMachine(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # services = forms.ModelChoiceField(queryset=Services.objects.all())
    model = Machines
    form_class = EditMachineForm
    template_name = 'machines/transfer_machine.html'
    success_url = reverse_lazy('machines:machines')

    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self):
        # self.id_ == machine_id
        self.id_ = self.kwargs.get("machine_id")  # apo to urls.py -->> path('<int:machine_id>'....
        machine = Machines.objects.all().filter(pk=self.id_)
        self.Προηγούμενος_Πελάτης = machine[0].Πελάτης
        return get_object_or_404(Machines, id=self.id_, )

    def get_initial(self):
        initial = super(TransferMachine, self).get_initial()
        try:
            old_date = self.object.Εναρξη
            new_date = datetime.strptime(old_date, '%d/%m/%Y').strftime('%Y-%m-%d')
            initial['Εναρξη'] = new_date
            return initial
        except ValueError as error:  # data '' does not match format '%d/%m/%Y'
            print("--------ValueError at Εναρξη -----------", __name__, "Function TransferMachine", error)
            return initial

    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("machine_id")
        context = super(TransferMachine, self).get_context_data(**kwargs)
        context['services'] = Services.objects.filter(Copier_ID=id_)  # whatever you would like

        dict_services = context['services'].values()
        try:
            sorted_services = sorted(dict_services, key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"),
                                     reverse=False)
            context['services'] = sorted_services
        except ValueError as error:
            print("--------ValueError at services -----------", __name__, "Function TransferMachine", error)
            pass
        except TypeError as error:
            print("--------TypeError at services -----------", __name__, "Function TransferMachine", error)
            pass
        # context['services'] = sorted_services
        context['machine_id'] = id_
        context['customer'] = Machines.objects.filter(pk=id_)
        return context

    def form_valid(self, form):
        if form.is_valid():
            data = form.cleaned_data
            Μηχάνημα = f"{data['Εταιρεία']}  Serial: {data['Serial']}"
            Ημερομηνία = datetime.today().strftime("%d/%m/%Y")
            Νέος_Πελάτης = data['Πελάτης']

            machine_Σημειώσεις = f"{data['Σημειώσεις']} \n -----Μεταφορα μηχανήματος----- απο πελάτη " \
                         f"{self.Προηγούμενος_Πελάτης} σε πελάτη {Νέος_Πελάτης} στης {Ημερομηνία}"

            Σημειώσεις = f"-----Μεταφορα μηχανήματος----- απο πελάτη " \
                         f"{self.Προηγούμενος_Πελάτης} σε πελάτη {Νέος_Πελάτης} στης {Ημερομηνία}"

            # Δημιουργεία Copiers_log
            new_service = CopiersLog.objects.create(Μηχάνημα=Μηχάνημα, Ημερομηνία=Ημερομηνία,
                                                    Προηγούμενος_Πελάτης=self.Προηγούμενος_Πελάτης,
                                                    Νέος_Πελάτης=Νέος_Πελάτης, Σημειώσεις=Σημειώσεις,
                                                    ID_μηχανήματος=self.object)

            form.instance.Σημειώσεις = machine_Σημειώσεις

        return super().form_valid(form)
