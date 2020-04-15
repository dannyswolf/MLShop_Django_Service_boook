"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import SparePartsListView, search_spareparts_view, EditSparePart

app_name = 'spareparts'
urlpatterns = [
    path('', SparePartsListView.as_view(), name='spareparts'),
    # path("add_service", CreateService.as_view(), name="add_service"),
    # path("add_service/<int:machine_id>", create_service_from_machines, name="add_service_from_machines"),
    #
    path('<int:spareparts_id>', EditSparePart.as_view(), name='edit_sparepart'),
    path('search_spareparts', search_spareparts_view,  name='search_spareparts'),
    # path('search_service_dte', search_services_dte,  name='search_services_dte'),
    # path('<int:service_id>/delete/', ServiceDelete.as_view(), name='delete_service'),
]
