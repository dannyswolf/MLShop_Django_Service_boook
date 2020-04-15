from django.forms import modelform_factory, TextInput, Textarea
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Calendar
from django.urls import reverse_lazy
from datetime import date, datetime
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from machines.models import Machines
from .forms import CreateCalendarForm, EditCalendarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from services.models import Services
from django.core.exceptions import ObjectDoesNotExist
from spareparts.models import SpareParts


# Ενεργά
class CalendarListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    model = Calendar
    template_name = 'Calendar/calendar_detail.html'
    # sorted(data_from_calendar, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y"))
    # queryset = sorted(Services.objects.all(), key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"))
    # sort(key=lambda date: datetime.strptime(date, '"%d/%m/%Y"))
    # queryset = Calendar.objects.filter(Κατάσταση=True).order_by('-pk')


    # print("context['services']", context['services'][1:])
    # sorted_data_from_calendar = sorted(data_from_calendar, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y"))
    # queryset = sorted(dict_services, key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"))
    fields = '__all__'
    # form_class = CustomerForm
    paginate_by = 5

    # -------- Sorting --------------
    def get_queryset(self,):
        queryset = Calendar.objects.filter(Κατάσταση=True)
        dict_services = queryset.values()
        queryset = sorted(dict_services, key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"))
        return queryset


# Ολοκληρωμένες εργασίες
class FinishedCalendarListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    model = Calendar
    template_name = 'Calendar/finished_jobs.html'
    fields = '__all__'
    # form_class = CustomerForm
    paginate_by = 7

    # -------- Sorting --------------
    def get_queryset(self,):
        queryset = Calendar.objects.filter(Κατάσταση=False)
        dict_services = queryset.values()
        queryset = sorted(dict_services, key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"), reverse=True)
        return queryset


@login_required()
def create_calendar(request, machine_id, **kwargs):
    machine = Machines.objects.all().filter(pk=machine_id)
    customer = machine[0].Πελάτης

    initial_data = {
        'Copier_ID': machine_id,
        'Customer_ID': customer.pk,
        'Πελάτης': customer,
        'Μηχάνημα': machine[0],
        'Τηλέφωνο': customer.Τηλέφωνο,


    }

    form = CreateCalendarForm(request.POST or None, initial=initial_data)

    if request.method == 'POST':
        if form.is_valid():

            data = form.cleaned_data
            Σκοπός = data['Σκοπός']
            Ενέργειες = data['Ενέργειες']
            Τεχνικός = data['Τεχνικός']
            Ημερομηνία = data['Ημ_Ολοκλ']
            ΔΤΕ = data['ΔΤΕ']
            Μετρητής = data['Μετρητής']
            Επ_Service = data['Επ_Service']
            Price = data['Price']
            Copier_ID_id = data['Copier_ID']
            Σημειώσεις = data['Σημειώσεις']
            # if  and (data['Service_ID'] is None or data['Service_ID'] == ""):
            # Αν είναι κενό η Ημερομηνία και τελειωμένη εργασία να πάρει σημερηνή ημερομηνία ολοκλήρωσης service
            if (Ημερομηνία is None or Ημερομηνία == "") and data['Κατάσταση'] is False:
                Ημερομηνία = date.today().strftime("%d/%m/%Y")
            else:  # αλλαγή απο YYYY-MM-DD (ετσι τα βγαζει ο φυλομετρητρης)  σε DD-MM-YYYY
                Ημερομηνία = datetime.strptime(Ημερομηνία, '%Y-%m-%d').strftime('%d/%m/%Y')

            # Δημιουργεία service
            new_service = Services.objects.create(Σκοπός_Επίσκεψης=Σκοπός, Ενέργειες=Ενέργειες, Τεχνικός=Τεχνικός,
                                                  Σημειώσεις=Σημειώσεις, Μετρητής=Μετρητής, Επ_Service=Επ_Service,
                                                  Price=Price, Copier_ID=Copier_ID_id, Ημερομηνία=Ημερομηνία, ΔΤΕ=ΔΤΕ)
            form.instance.Service_ID = new_service.pk
            form.instance.Ημ_Ολοκλ = date.today().strftime("%d/%m/%Y")

            form.save()

            return HttpResponseRedirect('../',)
    context = {
        'form': form,
    }

    return render(request, 'Calendar/create.html', context)


class EditCalendar(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''  # Αν δεν ειναι login ο χρήστης σε πάει στην αρχηκή /
    model = Calendar
    # Copier_ID_id = ChoiceField(disabled=True)

    # form_class = modelform_factory(Calendar,
    #                                widgets={
    #                                    "Ημερομηνία": TextInput(attrs={'type': 'date',}, ),
    #                                    'Ημ_Ολοκλ': TextInput(attrs={'type': 'date'}),
    #                                     'Σημειώσεις': Textarea(attrs={'cols': 40, 'rows': 15})
    #                                }, fields=('Ημερομηνία', 'Πελάτης', "Τηλέφωνο",
    #                                            "Copier_ID", "Σκοπός", "Ενέργειες", "Τεχνικός", "Επείγων",
    #                                            "Μετρητής", "Επ_Service", "ΔΤΕ", "Price", "Service_ID",
    #                                            "Σημειώσεις", "Ημ_Ολοκλ", "Κατάσταση"))
    form_class = EditCalendarForm
    template_name = 'Calendar/detail.html'
    success_url = reverse_lazy('Calendar:list_calendar')



    def get_object(self, queryset=None):
        id_ = self.kwargs.get("calendar_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(Calendar, id=id_)

    def get_initial(self):
        initial = super(EditCalendar, self).get_initial()

        try:
            old_date = self.object.Ημερομηνία
            new_date = datetime.strptime(old_date, '%d/%m/%Y').strftime('%Y-%m-%d')
            initial['Ημερομηνία'] = new_date
        except ValueError as error:
            print("--------ValueError at Ημερομηνία -----------", error)
            pass
        try:
            old_date = self.object.Ημ_Ολοκλ
            Ημ_Ολοκλ = datetime.strptime(old_date, '%d/%m/%Y').strftime('%Y-%m-%d')
            initial['Ημ_Ολοκλ'] = Ημ_Ολοκλ
        except ValueError as error:
            print("---------- ValueError at Ημ_Ολοκλ ----------", error)
        return initial

    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("calendar_id")
        context = super(EditCalendar, self).get_context_data(**kwargs)
        context['calendar_form'] = self.object  # whatever you would like

        spareparts = SpareParts.objects.filter(Calendar_ID=id_)
        context['spareparts'] = spareparts

        return context

    def form_valid(self, form):
        data = form.cleaned_data
        # Να ενημερώνει το service
        # if data['Κατάσταση'] is False and (data['Service_ID'] is None or data['Service_ID'] == ""):

        Σκοπός_Επίσκεψης = data['Σκοπός']
        Ενέργειες = data['Ενέργειες']
        Τεχνικός = data['Τεχνικός']
        Ημερομηνία = data['Ημ_Ολοκλ']
        ΔΤΕ = data['ΔΤΕ']
        Μετρητής = data['Μετρητής']
        Επ_Service = data['Επ_Service']
        Price = data['Price']
        Copier_ID = data['Copier_ID']
        Σημειώσεις = data['Σημειώσεις']
        Service_ID = data['Service_ID']
        if Ημερομηνία is None or Ημερομηνία == "":
            Ημερομηνία = date.today().strftime("%d/%m/%Y")

        # Δημιουργία service
        try:
            service_record = Services.objects.get(id=Service_ID)
        except ObjectDoesNotExist:  # Αν δεν υπάρχει service δεν ενημερωνει τίποτα
            return super().form_valid(form)
        service_record.Σκοπός_Επίσκεψης = Σκοπός_Επίσκεψης
        service_record.Ενέργειες = Ενέργειες
        service_record.Τεχνικός = Τεχνικός
        service_record.Σημειώσεις = Σημειώσεις
        service_record.Μετρητής = Μετρητής
        service_record.Επ_Service = Επ_Service
        service_record.Price = Price
        service_record.Copier_ID = Copier_ID
        service_record.Ημερομηνία = Ημερομηνία
        service_record.ΔΤΕ = ΔΤΕ
        service_record.save()
        # new_service = Services.objects.get(Σκοπός_Επίσκεψης=Σκοπός, Ενέργειες=Ενέργειες, Τεχνικός=Τεχνικός,
        #                                       Σημειώσεις=Σημειώσεις, Μετρητής=Μετρητής, Επ_Service=Επ_Service,
        #                                       Price=Price, Copier_ID=Copier_ID_id, Ημερομηνία=Ημερομηνία, ΔΤΕ=ΔΤΕ)
        # form.instance.Service_ID = new_service.pk
        # form.instance.Ημ_Ολοκλ = date.today().strftime("%d/%m/%Y")

        return super().form_valid(form)


class CalendarDelete(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = Calendar
    template_name = 'Calendar/confirm_delete.html'
    success_url = reverse_lazy('Calendar:list_calendar')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("calendar_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(Calendar, id=id_)

    def form_valid(self):
        pass


# Αναζήτηση με Κατάσταση=False
@login_required()
def search_finished_calendar(request):
    # all_objects = Customer.objects.all()
    object_list = {}
    # "q" ειναι το ονομα στην φορμα form του αρχείου customer_detail.html ---> <input name="q" ....
    # search_query ==> οτι πληκτρολογεί ο χρήστης για ανναζήτηση στο input με name="q"
    search_query = request.GET.get("q")
    if search_query != "" and search_query is not None:
        # __icontains  Case-insensitive Μη ευαίσθητο σε περίπτωση
        # __contains     Case-sensitive      Ευαίσθητα σε μικροσκοπικά
        # SQLite doesnt support case-sensitive
        all_objects = Calendar.objects.filter(
            Q(Ημερομηνία__icontains=search_query) |
            Q(Πελάτης__icontains=search_query) |
            Q(Μηχάνημα__icontains=search_query) |
            Q(Σκοπός__icontains=search_query) |
            Q(Ενέργειες__icontains=search_query) |
            Q(Τεχνικός__icontains=search_query) |
            Q(Τηλέφωνο__icontains=search_query) |
            Q(Σημειώσεις__icontains=search_query) |
            Q(ΔΤΕ__icontains=search_query)
        ).filter(Κατάσταση=False).order_by('Πελάτης')
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
    return render(request, "Calendar/search_calendar_result.html", object_list)


# Αναζήτηση με Κατάσταση=True
@login_required()
def search_calendar(request):
    # all_objects = Customer.objects.all()
    object_list = {}
    # "q" ειναι το ονομα στην φορμα form του αρχείου customer_detail.html ---> <input name="q" ....
    # search_query ==> οτι πληκτρολογεί ο χρήστης για ανναζήτηση στο input με name="q"
    search_query = request.GET.get("q")
    if search_query != "" and search_query is not None:
        # __icontains  Case-insensitive Μη ευαίσθητο σε περίπτωση
        # __contains     Case-sensitive      Ευαίσθητα σε μικροσκοπικά
        # SQLite doesnt support case-sensitive
        all_objects = Calendar.objects.filter(
            Q(Ημερομηνία__icontains=search_query) |
            Q(Πελάτης__icontains=search_query) |
            Q(Μηχάνημα__icontains=search_query) |
            Q(Σκοπός__icontains=search_query) |
            Q(Ενέργειες__icontains=search_query) |
            Q(Τεχνικός__icontains=search_query) |
            Q(Τηλέφωνο__icontains=search_query) |
            Q(Σημειώσεις__icontains=search_query) |
            Q(ΔΤΕ__icontains=search_query)
        ).filter(Κατάσταση=True).order_by('Πελάτης')
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
    return render(request, "Calendar/search_calendar_result.html", object_list)


# search ΔΤΕ
# Αναζήτηση με Κατάσταση=True
@login_required()
def search_calendar_dte(request):
    # all_objects = Customer.objects.all()
    object_list = {}
    # "q" ειναι το ονομα στην φορμα form του αρχείου customer_detail.html ---> <input name="q" ....
    # search_query ==> οτι πληκτρολογεί ο χρήστης για ανναζήτηση στο input με name="q"
    search_query = request.GET.get("q")
    if search_query != "" and search_query is not None:
        # __icontains  Case-insensitive Μη ευαίσθητο σε περίπτωση
        # __contains     Case-sensitive      Ευαίσθητα σε μικροσκοπικά
        # SQLite doesn’t support case-sensitive
        all_objects = Calendar.objects.filter(
            Q(ΔΤΕ__icontains=search_query)
        ).filter(Κατάσταση=True).order_by('Πελάτης')
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
    return render(request, "Calendar/search_calendar_result.html", object_list)


# search ΔΤΕ
# Αναζήτηση με Κατάσταση=False
@login_required()
def search_finished_calendar_dte(request):
    # all_objects = Customer.objects.all()
    object_list = {}
    # "q" ειναι το ονομα στην φορμα form του αρχείου customer_detail.html ---> <input name="q" ....
    # search_query ==> οτι πληκτρολογεί ο χρήστης για ανναζήτηση στο input με name="q"
    search_query = request.GET.get("q")
    if search_query != "" and search_query is not None:
        # __icontains  Case-insensitive Μη ευαίσθητο σε περίπτωση
        # __contains     Case-sensitive      Ευαίσθητα σε μικροσκοπικά
        # SQLite doesn’t support case-sensitive
        all_objects = Calendar.objects.filter(
            Q(ΔΤΕ__icontains=search_query)
        ).filter(Κατάσταση=False).order_by('Πελάτης')
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
    return render(request, "Calendar/search_calendar_result.html", object_list)
