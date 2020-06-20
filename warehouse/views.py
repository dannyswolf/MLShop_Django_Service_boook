# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import (A_ΟΡΟΦΟΣ, BROTHER, CANON, EPSON, KONICA, KYOCERA, LEXMARK, OKI, RICOH, SAMSUNG, SHARP,
                     ΜΕΛΑΝΑΚΙΑ, ΜΕΛΑΝΟΤΑΙΝΙΕΣ, ΤΟΝΕΡ, ΦΩΤΟΤΥΠΙΚΑ, ΧΧΧ)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django_project.settings import SPARE_PARTS_ROOT, SPARE_PARTS_URL
import os
import shutil
from django.http import HttpResponseRedirect, JsonResponse


@login_required()
def A_ΟΡΟΦΟΣ_json(request, *args, **kwargs):
    queryset = A_ΟΡΟΦΟΣ.objects.using('SparePartsDb').all()
    # qs_json = serializers.serialize('json', queryset)
    list_items = [{"id": x.id, "ΕΤΑΙΡΙΑ": str(x.ΕΤΑΙΡΙΑ), "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "TEMAXIA": x.TEMAXIA, "ΤΙΜΗ": x.ΤΙΜΗ, "ΣΥΝΟΛΟ": x.ΣΥΝΟΛΟ, "ΣΕΛΙΔΕΣ": x.ΣΕΛΙΔΕΣ,
                   "ΠΑΡΑΤΗΡΗΣΗΣ": x.ΠΑΡΑΤΗΡΗΣΗΣ} for x in queryset]
    
    status = 200
    data = {
        "response": list_items
    }
    # return JsonResponse(data=data, status=status)
    return JsonResponse(data=data, status=status)


class A_ΟΡΟΦΟΣListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/A_ΟΡΟΦΟΣ_detail.html'
    fields = '__all__'
    queryset = A_ΟΡΟΦΟΣ.objects.using('SparePartsDb').all()


class A_ΟΡΟΦΟΣCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = A_ΟΡΟΦΟΣ
    fields = '__all__'
    template_name = 'warehouse/add_A_ΟΡΟΦΟΣ.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:A_ΟΡΟΦΟΣ')


class A_ΟΡΟΦΟΣUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # machines = forms.ModelChoiceField(queryset=Machines.objects.all())
    model = A_ΟΡΟΦΟΣ
    fields = '__all__'
    template_name = 'warehouse/edit_A_ΟΡΟΦΟΣ.html'
    success_url = reverse_lazy('warehouse:A_ΟΡΟΦΟΣ')
    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(A_ΟΡΟΦΟΣ, id=id_)

    def get_context_data(self, **kwargs):
        context = super(A_ΟΡΟΦΟΣUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        # context['calendar_form'] = self.object  # whatever you would like
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class A_ΟΡΟΦΟΣDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = A_ΟΡΟΦΟΣ
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:A_ΟΡΟΦΟΣ')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(A_ΟΡΟΦΟΣ, id=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)
        

class BROTHERListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = BROTHER.objects.using('SparePartsDb').all()


@login_required()
def BROTHER_json(request, *args, **kwargs):
    queryset = BROTHER.objects.using('SparePartsDb').all()
    # qs_json = serializers.serialize('json', queryset)
    list_items = [{"ID": x.ID, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ,} for x in queryset]
    
    status = 200
    data = {
        "response": list_items
    }
    # return JsonResponse(data=data, status=status)
    return JsonResponse(data=data, status=status)


class BROTHERCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = BROTHER
    fields = '__all__'
    template_name = 'warehouse/add_photocopiers.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:brother',)


class BROTHERUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = BROTHER
    fields = '__all__'
    template_name = 'warehouse/edit_photocopiers.html'
    success_url = reverse_lazy('warehouse:brother')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(BROTHER, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(BROTHERUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class BROTHERDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = BROTHER
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:brother')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(BROTHER, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class CANONListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = CANON.objects.using('SparePartsDb').all()


@login_required()
def CANON_json(request, *args, **kwargs):
    queryset = CANON.objects.using('SparePartsDb').all()
    # qs_json = serializers.serialize('json', queryset)
    list_items = [{"id": x.ID, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ,} for x in queryset]
    
    status = 200
    data = {
        "response": list_items
    }
    # return JsonResponse(data=data, status=status)
    return JsonResponse(data=data, status=status)


class CANONCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = CANON
    fields = '__all__'
    template_name = 'warehouse/add_photocopiers.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:canon')


class CANONUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = CANON
    fields = '__all__'
    template_name = 'warehouse/edit_photocopiers.html'
    success_url = reverse_lazy('warehouse:canon')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(CANON, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(CANONUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class CANONDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = CANON
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:canon')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(CANON, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class EPSONListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = EPSON.objects.using('SparePartsDb').all()


@login_required()
def EPSON_json(request, *args, **kwargs):
    queryset = EPSON.objects.using('SparePartsDb').all()
    # qs_json = serializers.serialize('json', queryset)
    list_items = [{"id": x.ID, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ, } for x in queryset]

    status = 200
    data = {
        "response": list_items
    }
    # return JsonResponse(data=data, status=status)
    return JsonResponse(data=data, status=status)


class EPSONCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = EPSON
    fields = '__all__'
    template_name = 'warehouse/add_photocopiers.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:epson')


class EPSONUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = EPSON
    fields = '__all__'
    template_name = 'warehouse/edit_photocopiers.html'
    success_url = reverse_lazy('warehouse:epson')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(EPSON, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(EPSONUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class EPSONDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = EPSON
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:epson')

    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(EPSON, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class KONICAListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = KONICA.objects.using('SparePartsDb').all()


@login_required()
def KONICA_json(request, *args, **kwargs):
    queryset = KONICA.objects.using('SparePartsDb').all()
    # qs_json = serializers.serialize('json', queryset)
    list_items = [{"id": x.ID, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ,} for x in queryset]
    
    status = 200
    data = {
        "response": list_items
    }
    # return JsonResponse(data=data, status=status)
    return JsonResponse(data=data, status=status)


class KONICACreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = KONICA
    fields = '__all__'
    template_name = 'warehouse/add_photocopiers.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:konica')


class KONICAUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = KONICA
    fields = '__all__'
    template_name = 'warehouse/edit_photocopiers.html'
    success_url = reverse_lazy('warehouse:konica')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(KONICA, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(KONICAUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class KONICADeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = KONICA
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:canon')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(KONICA, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class KYOCERAListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = KYOCERA.objects.using('SparePartsDb').all()


@login_required()
def KYOCERA_json(request, *args, **kwargs):
    queryset = KYOCERA.objects.using('SparePartsDb').all()
    # qs_json = serializers.serialize('json', queryset)
    list_items = [{"ID": x.pk, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ, } for x in queryset]

    status = 200
    data = {
        "response": list_items
    }
    # return JsonResponse(data=data, status=status)
    return JsonResponse(data=data, status=status)


class KYOCERACreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = KYOCERA
    fields = '__all__'
    template_name = 'warehouse/add_photocopiers.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:kyocera')


class KYOCERAUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = KYOCERA
    fields = '__all__'
    template_name = 'warehouse/edit_photocopiers.html'
    success_url = reverse_lazy('warehouse:kyocera')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(KYOCERA, id=id_)

    def get_context_data(self, **kwargs):
        context = super(KYOCERAUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class KYOCERADeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = KYOCERA
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:kyocera')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(KYOCERA, id=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class LEXMARKListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = LEXMARK.objects.using('SparePartsDb').all()


@login_required()
def LEXMARK_json(request, *args, **kwargs):
    queryset = LEXMARK.objects.using('SparePartsDb').all()
    list_items = [{"ID": x.pk, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ, } for x in queryset]

    status = 200
    data = {
        "response": list_items
    }

    return JsonResponse(data=data, status=status)


class LEXMARKCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = LEXMARK
    fields = '__all__'
    template_name = 'warehouse/add_photocopiers.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:lexmark')


class LEXMARKUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = LEXMARK
    fields = '__all__'
    template_name = 'warehouse/edit_photocopiers.html'
    success_url = reverse_lazy('warehouse:lexmark')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(LEXMARK, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(LEXMARKUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class LEXMARKDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = LEXMARK
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:lexmark')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(LEXMARK, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class OKIListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = OKI.objects.using('SparePartsDb').all()


@login_required()
def OKI_json(request, *args, **kwargs):
    queryset = OKI.objects.using('SparePartsDb').all()
    list_items = [{"ID": x.pk, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ, } for x in queryset]

    status = 200
    data = {
        "response": list_items
    }

    return JsonResponse(data=data, status=status)


class OKICreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = OKI
    fields = '__all__'
    template_name = 'warehouse/add_photocopiers.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:oki')


class OKIUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = OKI
    fields = '__all__'
    template_name = 'warehouse/edit_photocopiers.html'
    success_url = reverse_lazy('warehouse:oki')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(OKI, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(OKIUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class OKIDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = OKI
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:lexmark')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(OKI, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class RICOHListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = RICOH.objects.using('SparePartsDb').all()


@login_required()
def RICOH_json(request, *args, **kwargs):
    queryset = RICOH.objects.using('SparePartsDb').all()
    list_items = [{"ID": x.pk, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ, } for x in queryset]

    status = 200
    data = {
        "response": list_items
    }

    return JsonResponse(data=data, status=status)


class RICOHCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = RICOH
    fields = '__all__'
    template_name = 'warehouse/add_photocopiers.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:ricoh')


class RICOHUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = RICOH
    fields = '__all__'
    template_name = 'warehouse/edit_photocopiers.html'
    success_url = reverse_lazy('warehouse:ricoh')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(RICOH, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(RICOHUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class RICOHDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = RICOH
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:ricoh')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(RICOH, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class SAMSUNGListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = SAMSUNG.objects.using('SparePartsDb').all()


@login_required()
def SAMSUNG_json(request, *args, **kwargs):
    queryset = SAMSUNG.objects.using('SparePartsDb').all()
    list_items = [{"ID": x.pk, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ, } for x in queryset]

    status = 200
    data = {
        "response": list_items
    }

    return JsonResponse(data=data, status=status)


class SAMSUNGCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = SAMSUNG
    fields = '__all__'
    template_name = 'warehouse/add_photocopiers.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:samsung')


class SAMSUNGUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = SAMSUNG
    fields = '__all__'
    template_name = 'warehouse/edit_photocopiers.html'
    success_url = reverse_lazy('warehouse:samsung')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(SAMSUNG, id=id_)

    def get_context_data(self, **kwargs):
        context = super(SAMSUNGUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class SAMSUNGDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = SAMSUNG
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:samsung')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(SAMSUNG, id=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class SHARPListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/photocopiers_detail.html'
    fields = '__all__'
    queryset = SHARP.objects.using('SparePartsDb').all()


@login_required()
def SHARP_json(request, *args, **kwargs):
    queryset = SHARP.objects.using('SparePartsDb').all()
    list_items = [{"ID": x.pk, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ, } for x in queryset]

    status = 200
    data = {
        "response": list_items
    }

    return JsonResponse(data=data, status=status)


class SHARPCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = SHARP
    fields = '__all__'
    template_name = 'warehouse/add_photocopiers.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:sharp')


class SHARPUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = SHARP
    fields = '__all__'
    template_name = 'warehouse/edit_photocopiers.html'
    success_url = reverse_lazy('warehouse:sharp')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(SHARP, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(SHARPUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class SHARPDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = SHARP
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:sharp')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(SHARP, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class ΜΕΛΑΝΑΚΙΑListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/inks_toner_detail.html'
    fields = '__all__'
    queryset = ΜΕΛΑΝΑΚΙΑ.objects.using('SparePartsDb').all()


@login_required()
def ΜΕΛΑΝΑΚΙΑ_json(request, *args, **kwargs):
    queryset = ΜΕΛΑΝΑΚΙΑ.objects.using('SparePartsDb').all()
    list_items = [{"ID": x.pk, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ, } for x in queryset]

    status = 200
    data = {
        "response": list_items
    }

    return JsonResponse(data=data, status=status)


class ΜΕΛΑΝΑΚΙΑCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = ΜΕΛΑΝΑΚΙΑ
    fields = '__all__'
    template_name = 'warehouse/add_inks_toner.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:melanakia')


class ΜΕΛΑΝΑΚΙΑUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # machines = forms.ModelChoiceField(queryset=Machines.objects.all())
    model = ΜΕΛΑΝΑΚΙΑ
    fields = '__all__'
    template_name = 'warehouse/edit_inks_toner.html'
    success_url = reverse_lazy('warehouse:melanakia')
    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(ΜΕΛΑΝΑΚΙΑ, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(ΜΕΛΑΝΑΚΙΑUpdateView, self).get_context_data(**kwargs)

        try:

            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, self.object.get_path()))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):

            def process(f):

                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class ΜΕΛΑΝΑΚΙΑDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = ΜΕΛΑΝΑΚΙΑ
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:melanakia')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(ΜΕΛΑΝΑΚΙΑ, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())


        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class ΜΕΛΑΝΟΤΑΙΝΙΕΣListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/melanotainies_detail.html'
    fields = '__all__'
    queryset = ΜΕΛΑΝΟΤΑΙΝΙΕΣ.objects.using('SparePartsDb').all()


@login_required()
def ΜΕΛΑΝΟΤΑΙΝΙΕΣ_json(request, *args, **kwargs):
    queryset = ΜΕΛΑΝΟΤΑΙΝΙΕΣ.objects.using('SparePartsDb').all()
    list_items = [{"ID": x.pk, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ, } for x in queryset]

    status = 200
    data = {
        "response": list_items
    }

    return JsonResponse(data=data, status=status)


class ΜΕΛΑΝΟΤΑΙΝΙΕΣCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = ΜΕΛΑΝΟΤΑΙΝΙΕΣ
    fields = '__all__'
    template_name = 'warehouse/add_melanotainies.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:melanotainies')


class ΜΕΛΑΝΟΤΑΙΝΙΕΣUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = ΜΕΛΑΝΟΤΑΙΝΙΕΣ
    fields = '__all__'
    template_name = 'warehouse/edit_melanotainies.html'
    success_url = reverse_lazy('warehouse:melanotainies')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(ΜΕΛΑΝΟΤΑΙΝΙΕΣ, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(ΜΕΛΑΝΟΤΑΙΝΙΕΣUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class ΜΕΛΑΝΟΤΑΙΝΙΕΣDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = ΜΕΛΑΝΟΤΑΙΝΙΕΣ
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:melanotainies')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(ΜΕΛΑΝΟΤΑΙΝΙΕΣ, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class ΤΟΝΕΡListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/inks_toner_detail.html'
    fields = '__all__'
    queryset = ΤΟΝΕΡ.objects.using('SparePartsDb').all()


@login_required()
def ΤΟΝΕΡ_json(request, *args, **kwargs):
    queryset = ΤΟΝΕΡ.objects.using('SparePartsDb').all()
    list_items = [{"ID": x.pk, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ, } for x in queryset]

    status = 200
    data = {
        "response": list_items
    }

    return JsonResponse(data=data, status=status)


class ΤΟΝΕΡCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = ΤΟΝΕΡ
    fields = '__all__'
    template_name = 'warehouse/add_inks_toner.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:toner')


class ΤΟΝΕΡUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # machines = forms.ModelChoiceField(queryset=Machines.objects.all())
    model = ΤΟΝΕΡ
    fields = '__all__'
    template_name = 'warehouse/edit_inks_toner.html'
    success_url = reverse_lazy('warehouse:toner')
    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(ΤΟΝΕΡ, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(ΤΟΝΕΡUpdateView, self).get_context_data(**kwargs)

        try:

            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, self.object.get_path()))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):

            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class ΤΟΝΕΡDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = ΤΟΝΕΡ
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:toner')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(ΤΟΝΕΡ, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()

        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())
        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class ΦΩΤΟΤΥΠΙΚΑListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/inks_toner_detail.html'
    fields = '__all__'
    queryset = ΦΩΤΟΤΥΠΙΚΑ.objects.using('SparePartsDb').all()


@login_required()
def ΦΩΤΟΤΥΠΙΚΑ_json(request, *args, **kwargs):
    queryset = ΦΩΤΟΤΥΠΙΚΑ.objects.using('SparePartsDb').all()
    list_items = [{"ID": x.pk, "ΠΕΡΙΓΡΑΦΗ": str(x.ΠΕΡΙΓΡΑΦΗ), "ΚΩΔΙΚΟΣ": str(x.ΚΩΔΙΚΟΣ),
                   "ΤΕΜΑΧΙΑ": x.ΤΕΜΑΧΙΑ, } for x in queryset]

    status = 200
    data = {
        "response": list_items
    }

    return JsonResponse(data=data, status=status)


class ΦΩΤΟΤΥΠΙΚΑCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = ΦΩΤΟΤΥΠΙΚΑ
    fields = '__all__'
    template_name = 'warehouse/add_inks_toner.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:fototipika')


class ΦΩΤΟΤΥΠΙΚΑUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    # machines = forms.ModelChoiceField(queryset=Machines.objects.all())
    model = ΦΩΤΟΤΥΠΙΚΑ
    fields = '__all__'
    template_name = 'warehouse/edit_inks_toner.html'
    success_url = reverse_lazy('warehouse:fototipika')
    # queryset = Customer.objects.get()
    # form_class = CustomerForm  # modelform

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(ΦΩΤΟΤΥΠΙΚΑ, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(ΦΩΤΟΤΥΠΙΚΑUpdateView, self).get_context_data(**kwargs)

        try:

            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, self.object.get_path()))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):

            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class ΦΩΤΟΤΥΠΙΚΑDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = ΦΩΤΟΤΥΠΙΚΑ
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:fototipika')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(ΦΩΤΟΤΥΠΙΚΑ, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()

        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())
        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)


class ΧΧΧListView(LoginRequiredMixin, ListView):
    redirect_field_name = ''
    template_name = 'warehouse/xxx_detail.html'
    fields = '__all__'
    queryset = ΧΧΧ.objects.using('SparePartsDb').all()


class ΧΧΧCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = ''
    model = ΧΧΧ
    fields = '__all__'
    template_name = 'warehouse/add_xxx.html'

    def get_success_url(self):
        return reverse_lazy('warehouse:xxx')

class ΧΧΧUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = ''
    model = ΧΧΧ
    fields = '__all__'
    template_name = 'warehouse/edit_xxx.html'
    success_url = reverse_lazy('warehouse:xxx')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:customer_id>'....
        return get_object_or_404(ΧΧΧ, ID=id_)

    def get_context_data(self, **kwargs):
        context = super(ΧΧΧUpdateView, self).get_context_data(**kwargs)
        path = self.object.get_path()
        try:
            files = os.listdir(os.path.join(SPARE_PARTS_ROOT, path))
            context['files'] = files

        except FileNotFoundError as error:  # Όταν δεν υπάρχουν αρχεία
            context['files'] = ""
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        path = self.object.get_path()
        # Αρχεία
        file_dir = os.path.join(SPARE_PARTS_ROOT, path)

        # Αν ανεβάσουμε αρχεία να κάνει φάκελο αν δεν υπάρχει
        if self.request.FILES.getlist("file") and not os.path.exists(file_dir):
            os.makedirs(file_dir)

        for x in self.request.FILES.getlist("file"):
            def process(f):
                with open(f'{file_dir}/' + str(f.name), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            process(x)

        return super().form_valid(form)


class XXXDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name = ''
    model = ΧΧΧ
    template_name = 'warehouse/confirm_delete.html'
    success_url = reverse_lazy('warehouse:xxx')
    # error_url = 'customers/error_url.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("spare_part_id")  # apo to urls.py -->> path('<int:service_id>'....
        return get_object_or_404(ΧΧΧ, ID=id_)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        path_to_delete = os.path.join(SPARE_PARTS_ROOT, self.object.get_path())

        try:
            shutil.rmtree(path_to_delete, ignore_errors=True)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

        self.object.delete()
        return HttpResponseRedirect(success_url)