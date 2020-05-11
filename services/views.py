import os
from django_project.settings import MEDIA_ROOT
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Services
from django.urls import reverse_lazy
from django.forms import Textarea
from django.forms.models import modelform_factory
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from machines.models import Machines
from services.forms import CreateServiceFromMachineForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from spareparts.models import SpareParts
from datetime import datetime


class ServicesListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    # model = Services
    template_name = 'services/services_detail.html'

    fields = '__all__'
    # form_class = CustomerForm
    # paginate_by = 10
    queryset = Services.objects.select_related('Copier_ID').prefetch_related('Copier_ID__Πελάτης')
    # -------- Sorting --------------
    # def get_queryset(self,):
    #     queryset = Services.objects.select_related('Copier_ID').prefetch_related('Copier_ID__Πελάτης')
    #
    #     # dict_services = queryset.values()
    #     # queryset = sorted(dict_services, key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"))
    #     return queryset


class EditService(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = Services
    # Copier_ID_id = ChoiceField(disabled=True)

    # fields = ('Ημερομηνία', 'Σκοπός_Επίσκεψης', 'Ενέργειες', 'Τεχνικός', 'Μετρητής', 'Επ_Service', 'ΔΤΕ', 'Price',
    #           'Σημειώσεις')
    form_class = modelform_factory(Services,
                                   widgets={
                                            "Σημειώσεις": Textarea(attrs={'cols': 40, 'rows': 15})
                                            }, fields=('Ημερομηνία', 'Σκοπός_Επίσκεψης', 'Ενέργειες', 'Τεχνικός',
                                                       'Μετρητής', 'Επ_Service', 'ΔΤΕ', 'Price',  'Σημειώσεις'))
    template_name = 'services/detail.html'
    success_url = reverse_lazy('services:services')
    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("service_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(Services, id=id_)

    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("service_id")
        context = super(EditService, self).get_context_data(**kwargs)
        context['machine_form'] = self.object  # whatever you would like
        spareparts = SpareParts.objects.filter(Service_ID=id_)
        context['service_id'] = id_
        try:
            files = os.listdir(os.path.join(MEDIA_ROOT, str(id_)))
            context['files'] = files
        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""

        context['spareparts'] = spareparts

        return context

    def form_valid(self, form):
        # # Αρχεία
        Service_ID = form.instance.id
        file_dir = os.path.join(MEDIA_ROOT, str(Service_ID))
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        for x in self.request.FILES.getlist("file"):

            def process(f):

                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
            process(x)
        return super().form_valid(form)


class ServiceDelete(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = Services
    template_name = 'services/confirm_delete.html'
    success_url = reverse_lazy('services:services')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("service_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(Services, id=id_)


@login_required()
def search_service_view(request):
    # all_objects = Customer.objects.all()

    object_list = {}
    # "q" ειναι το ονομα στην φορμα form του αρχείου customer_detail.html ---> <input name="q" ....
    # search_query ==> οτι πληκτρολογεί ο χρήστης για ανναζήτηση στο input με name="q"
    search_query = request.GET.get("q")
    if search_query != "" and search_query is not None:
        # __icontains  Case-insensitive Μη ευαίσθητο σε περίπτωση
        # __contains     Case-sensitive      Ευαίσθητα σε μικροσκοπικά
        # SQLite doesnt support case-sensitive
        all_objects = Services.objects.filter(
            Q(Ημερομηνία__icontains=search_query) |
            Q(Σκοπός_Επίσκεψης__icontains=search_query) |
            Q(Ενέργειες__icontains=search_query) |
            Q(Τεχνικός__icontains=search_query) |
            Q(Σημειώσεις__icontains=search_query) |
            # Make sure you are not adding any Foreignkey or ManyToManyField to your search_field directly.
            # Use Django's double underscore convention instead.
            # https://docs.djangoproject.com/en/3.0/topics/db/queries/#lookups-that-span-relationships
            Q(Copier_ID__Πελάτης__Επωνυμία_Επιχείρησης__icontains=search_query) |
            Q(Copier_ID__Serial__icontains=search_query) |
            Q(Copier_ID__Εταιρεία__icontains=search_query) |
            Q(ΔΤΕ__icontains=search_query)
        ).order_by('Copier_ID__Πελάτης__Επωνυμία_Επιχείρησης')
        paginator = Paginator(all_objects, 6)  # 10 posts per page
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
    return render(request, "services/search_service_result.html", object_list)


@login_required()
def create_service_from_machines(request, machine_id, **kwargs):
    machine = Machines.objects.all().filter(pk=machine_id)
    customer = machine[0].Πελάτης
    initial_data = {
        'Copier_ID': machine[0]
    }

    success_url = reverse_lazy('services:edit_service')
    form = CreateServiceFromMachineForm(request.POST or None, initial=initial_data)
    if request.method == 'POST':
        if form.is_valid():

            form.save()

            # # Αρχεία
            Service_ID = form.instance.id

            file_dir = os.path.join(MEDIA_ROOT, str(Service_ID))
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            for x in request.FILES.getlist("file"):

                def process(f):
                    with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)
                process(x)

            return HttpResponseRedirect('../',)
    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, 'services/create_service_from_machines.html', context)


@login_required()
def search_services_dte(request):
    # all_objects = Customer.objects.all()

    object_list = {}
    # "q" ειναι το ονομα στην φορμα form του αρχείου customer_detail.html ---> <input name="q" ....
    # search_query ==> οτι πληκτρολογεί ο χρήστης για ανναζήτηση στο input με name="q"
    search_query = request.GET.get("q")
    if search_query != "" and search_query is not None:
        # __icontains  Case-insensitive Μη ευαίσθητο σε περίπτωση
        # __contains     Case-sensitive      Ευαίσθητα σε μικροσκοπικά
        # SQLite doesnt support case-sensitive
        all_objects = Services.objects.filter(
            Q(ΔΤΕ__icontains=search_query)
        ).order_by('Copier_ID__Πελάτης__Επωνυμία_Επιχείρησης')
        paginator = Paginator(all_objects, 6)  # 10 posts per page
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
    return render(request, "services/search_service_result.html", object_list)
