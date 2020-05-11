from django.views.generic import ListView, UpdateView
from .models import SpareParts
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.forms.models import modelform_factory
from django.forms import Textarea
from machines.models import Machines


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
