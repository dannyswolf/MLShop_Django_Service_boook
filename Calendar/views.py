import calendar
import os
import shutil
from datetime import date, datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from django_project.settings import MEDIA_ROOT

from machines.models import Machines
from services.models import Services
from spareparts.models import SpareParts

from .forms import CreateCalendarForm, EditCalendarForm
from .models import Calendar
from .utils import MyFinishedHtmlCalendar, MyHtmlCalendar


@login_required()
def delete_files(request, *args, **kwargs):
    service_id = kwargs['service_id']
    calendar_object = Calendar.objects.get(Service_ID=service_id)
    calendar_date = calendar_object.Ημερομηνία
    calendar_year = calendar_date[6:]
    calendar_id = calendar_object.pk

    data = {
        'service_id': service_id,
        'object': calendar_object
    }
    if request.method == "POST":
        path_to_delete = os.path.join(MEDIA_ROOT, f"{calendar_year}", str(service_id))
        shutil.rmtree(path_to_delete, ignore_errors=True)

        return HttpResponseRedirect(reverse('Calendar:edit_calendar', args=(calendar_id,)))

    return render(request, 'Calendar/confirm_delete-files.html', data)


# Ενεργά
class CalendarListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    model = Calendar
    template_name = 'Calendar/calendar_detail.html'
    fields = '__all__'
    # form_class = CustomerForm
    # paginate_by = 5

    # -------- Sorting --------------
    def get_queryset(self, ):
        """
        return : object_list
        """
        queryset = Calendar.objects.filter(Κατάσταση=True)
        # dict_services = queryset.values()
        # queryset = sorted(dict_services, key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"))

        return queryset


# Ολοκληρωμένες εργασίες
class FinishedCalendarListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    model = Calendar
    template_name = 'Calendar/finished_jobs.html'
    fields = '__all__'
    # form_class = CustomerForm
    # paginate_by = 7

    # -------- Sorting --------------
    def get_queryset(self, ):
        """
                return : object_list

                """
        queryset = Calendar.objects.filter(Κατάσταση=False)
        # dict_services = queryset.values()
        # queryset = sorted(dict_services, key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"), reverse=True)
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
                                                  Price=Price, Copier_ID=Copier_ID_id, Ημερομηνία=Ημερομηνία, ΔΤΕ=ΔΤΕ,
                                                  )
            form.instance.Service_ID = new_service.pk

            # Αρχεία
            # uploaded_file = request.FILES.getlist("file")
            Service_ID = new_service.pk
            file_dir = os.path.join(MEDIA_ROOT, f"{Ημερομηνία[6:]}", str(Service_ID))
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            for x in request.FILES.getlist("file"):

                def process(f):
                    with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)

                process(x)

            form.instance.Ημ_Ολοκλ = date.today().strftime("%d/%m/%Y")

            form.save()

            return HttpResponseRedirect('../', )
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
            print("--------ValueError at Ημερομηνία -----------", __file__, error)
            pass
        try:
            old_date = self.object.Ημ_Ολοκλ
            Ημ_Ολοκλ = datetime.strptime(old_date, '%d/%m/%Y').strftime('%Y-%m-%d')
            initial['Ημ_Ολοκλ'] = Ημ_Ολοκλ
        except ValueError as error:
            print("---------- ValueError at Ημ_Ολοκλ ----------", __file__, error)
        return initial

    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("calendar_id")
        context = super(EditCalendar, self).get_context_data(**kwargs)
        context['calendar_form'] = self.object  # whatever you would like
        try:

            files = os.listdir(os.path.join(MEDIA_ROOT, f"{self.object.Ημερομηνία[6:]}", str(self.object.Service_ID)))
            context['files'] = files
        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""

        spareparts = SpareParts.objects.filter(Service_ID=self.object.Service_ID)
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
        year = data['Ημερομηνία']
        ΔΤΕ = data['ΔΤΕ']
        Μετρητής = data['Μετρητής']
        Επ_Service = data['Επ_Service']
        Price = data['Price']
        Σημειώσεις = data['Σημειώσεις']
        Service_ID = data['Service_ID']

        # Αρχεία
        file_dir = os.path.join(MEDIA_ROOT, f"{year[6:]}", str(Service_ID))
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):

            def process(f):

                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

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
        self.id_ = self.kwargs.get("calendar_id")  # apo to urls.py -->> path('<int:service_id>'....
        # self.service_to_delete =
        # print("self.service_to_delete", self.service_to_delete)
        return get_object_or_404(Calendar, id=self.id_)

    def delete(self, request, *args, **kwargs):
        """
        Τρέχει όταν επιβεβαιώνουμε την διαγραφή
        self ==>  <Calendar.views.CalendarDelete object at 0x7fbc61c77908>
        request ==>       <WSGIRequest: POST '/Calendar/170/delete/'>
        kwargs ==>        {'calendar_id': 170}
        """
        self.object = self.get_object()
        # Διαγραφή Service
        service_to_delete = Services.objects.get(id=self.object.Service_ID)
        service_to_delete.delete()
        # Διαγραφή Calendar
        self.object.delete()
        return HttpResponseRedirect(self.success_url)


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
        # SQLite doesnt support case-sensitive
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


class CalendarView(LoginRequiredMixin, ListView):
    model = Calendar
    template_name = 'Calendar/HTMLCalendar.html'
    success_url = reverse_lazy("Calendar")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))
        new_month = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(new_month)
        context['next_month'] = next_month(new_month)

        # Instantiate our calendar class with today's year and date
        if new_month:
            cal = MyHtmlCalendar(d.year, new_month.month)
        else:
            cal = MyHtmlCalendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)

        return context


class FinishedCalendarView(LoginRequiredMixin, ListView):
    model = Calendar
    template_name = 'Calendar/FinishedHTMLCalendar.html'
    success_url = reverse_lazy("Calendar")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))
        new_month = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(new_month)
        context['next_month'] = next_month(new_month)

        # Instantiate our calendar class with today's year and date
        if new_month:
            cal = MyFinishedHtmlCalendar(d.year, new_month.month)
        else:
            cal = MyFinishedHtmlCalendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)

        return context


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    # calendar ==> import calendar (build in python)
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    """
        import calendar (build in python)
        calendar.monthrange(year, month)
        Returns weekday of first day of the month and number of days in month, for the specified year and month.
    """

    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
