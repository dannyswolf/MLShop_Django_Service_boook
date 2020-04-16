from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import CopiersLog


class CopiersLogListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    model = CopiersLog
    template_name = 'Copiers_Log/transfer_history.html'
    queryset = CopiersLog.objects.all().order_by('-id')

    fields = '__all__'
    # form_class = CustomerForm
    paginate_by = 5

