from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Customer
from machines.models import Machines
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from spareparts.models import SpareParts

# Create your views here.
# Always return an HttpResponseRedirect after successfully dealing
# with POST data. This prevents data from being posted twice if a
# user hits the Back button.


# Αναζήτηση ενεργών πελατων
@login_required()
def search_customer_view(request):
    # all_objects = Customer.objects.all()
    paginate_by = 20
    object_list = {}
    # "q" ειναι το ονομα στην φορμα form του αρχείου customer_detail.html ---> <input name="q" ....
    # search_query ==> οτι πληκτρολογεί ο χρήστης για ανναζήτηση στο input με name="q"
    search_query = request.GET.get("q")
    if search_query != "" and search_query is not None:
        # __icontains  Case-insensitive Μη ευαίσθητο σε περίπτωση
        # __contains     Case-sensitive      Ευαίσθητα σε μικροσκοπικά
        # SQLite doesnt support case-sensitive
        all_objects = Customer.objects.filter(Κατάσταση=True).filter(
            Q(Επωνυμία_Επιχείρησης__icontains=search_query) |
            Q(Ονοματεπώνυμο__icontains=search_query) |
            Q(Διεύθυνση__icontains=search_query) |
            Q(Πόλη__icontains=search_query) |
            Q(Περιοχή__icontains=search_query) |
            Q(Τηλέφωνο__icontains=search_query) |
            Q(Κινητό__icontains=search_query) |
            Q(Σημειώσεις__icontains=search_query)
        )
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
    # if not all_objects:
    #     all_objects = Customer.objects.all()
    #     return  render(request, "customers/customers_detail.html", {"object": all_objects})
    # το "object_list" ειναι το ´κλειδί' που οριζουμε στα δεδομένα  all_objects για να παρει το αρχείο
    # search_customer_result.html
        object_list = {"object_list": all_objects}
    return render(request, "customers/search_customer_result.html", object_list)


# Αναζήτηση ανενεργών πελατων
@login_required()
def search_inactive_customer_view(request):
    # all_objects = Customer.objects.all()
    paginate_by = 20
    object_list = {}
    # "q" ειναι το ονομα στην φορμα form του αρχείου customer_detail.html ---> <input name="q" ....
    # search_query ==> οτι πληκτρολογεί ο χρήστης για ανναζήτηση στο input με name="q"
    search_query = request.GET.get("q")
    if search_query != "" and search_query is not None:
        # __icontains  Case-insensitive Μη ευαίσθητο σε περίπτωση
        # __contains     Case-sensitive      Ευαίσθητα σε μικροσκοπικά
        # SQLite doesnt support case-sensitive
        all_objects = Customer.objects.filter(Κατάσταση=False).filter(
            Q(Επωνυμία_Επιχείρησης__icontains=search_query) |
            Q(Ονοματεπώνυμο__icontains=search_query) |
            Q(Διεύθυνση__icontains=search_query) |
            Q(Πόλη__icontains=search_query) |
            Q(Περιοχή__icontains=search_query) |
            Q(Τηλέφωνο__icontains=search_query) |
            Q(Κινητό__icontains=search_query) |
            Q(Σημειώσεις__icontains=search_query)
        )
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
        # if not all_objects:
        #     all_objects = Customer.objects.all()
        #     return  render(request, "customers/customers_detail.html", {"object": all_objects})
        # το "object_list" ειναι το ´κλειδί' που οριζουμε στα δεδομένα  all_objects για να παρει το αρχείο
        # search_customer_result.html
        object_list = {"object_list": all_objects}
    return render(request, "customers/search_customer_result.html", object_list)


# Ενεργοί πελάτες
class CreateCustomer(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    form_class = modelform_factory(Customer, fields='__all__')

    template_name = 'customers/create.html'

    def get_success_url(self):
        return reverse_lazy('customers:edit_customer', args=(self.object.id,))


# Ενεργοί πελάτες
class CustomersListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    # model = Customer
    template_name = 'customers/customers_detail.html'
    queryset = Customer.objects.filter(Κατάσταση=True)
    fields = '__all__'
    # form_class = CustomerForm
    # paginate_by = 5


# Ανενεργοί πελάτες
class InactiveCustomersListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    # model = Customer
    template_name = 'customers/inactive_customers_detail.html'
    queryset = Customer.objects.filter(Κατάσταση=False)
    fields = '__all__'
    # form_class = CustomerForm
    # paginate_by = 5


class EditCustomer(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # machines = forms.ModelChoiceField(queryset=Machines.objects.all())
    model = Customer
    fields = '__all__'
    template_name = 'customers/detail.html'
    success_url = reverse_lazy('customers:list_customers')
    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("customer_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(Customer, id=id_)

    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("customer_id")
        context = super(EditCustomer, self).get_context_data(**kwargs)
        context['machine_form'] = Machines.objects.filter(Πελάτης=id_)  # whatever you would like
        context['customer'] = id_
        context['spareparts'] = SpareParts.objects.filter(Customer_ID=id_)
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class CustomerDelete(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = Customer
    template_name = 'customers/confirm_delete.html'
    success_url = reverse_lazy('customers:list_customers')
    error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("customer_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(Customer, id=id_)


