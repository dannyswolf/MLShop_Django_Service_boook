from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import CopiersLog
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CopiersLogListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    model = CopiersLog
    template_name = 'Copiers_Log/transfer_history.html'
    queryset = CopiersLog.objects.all()

    fields = '__all__'
    # form_class = CustomerForm
    # paginate_by = 5


# Αναζήτηση
@login_required()
def search_copiers_log(request):
    # all_objects = Customer.objects.all()
    object_list = {}
    # "q" ειναι το ονομα στην φορμα form του αρχείου customer_detail.html ---> <input name="q" ....
    # search_query ==> οτι πληκτρολογεί ο χρήστης για ανναζήτηση στο input με name="q"
    search_query = request.GET.get("q")
    if search_query != "" and search_query is not None:
        # __icontains  Case-insensitive Μη ευαίσθητο σε περίπτωση
        # __contains     Case-sensitive      Ευαίσθητα σε μικροσκοπικά
        # SQLite doesnt support case-sensitive

        all_objects = CopiersLog.objects.filter(
            # Q(ID_μηχανήματος__icontains=search_query) |
            Q(Μηχάνημα__icontains=search_query) |
            Q(Ημερομηνία__icontains=search_query) |
            Q(Προηγούμενος_Πελάτης__icontains=search_query) |
            Q(Νέος_Πελάτης__icontains=search_query) |
            Q(Σημειώσεις__icontains=search_query)
        )
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
    return render(request, "Copiers_Log/search_copiers_log.html", object_list)