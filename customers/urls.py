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
from .views import CustomersListView, CreateCustomer, search_customer_view, EditCustomer, CustomerDelete, \
    InactiveCustomersListView, search_inactive_customer_view


app_name = 'customers'
urlpatterns = [
    path("", CustomersListView.as_view(), name="list_customers"),
    path("inactive", InactiveCustomersListView.as_view(), name="inactive_list_customers"),
    path("add_customer", CreateCustomer.as_view(), name="add_customer"),
    path('<int:customer_id>', EditCustomer.as_view(), name='edit_customer'),
    path('<int:customer_id>/delete/', CustomerDelete.as_view(), name='delete_customer'),
    path('search_customer', search_customer_view,  name='search_customer'),
    path('search_inactive_customer', search_inactive_customer_view,  name='search_inactive_customer'),

]
