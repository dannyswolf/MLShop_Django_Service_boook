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
from .views import (CalendarListView, create_calendar, EditCalendar, FinishedCalendarListView, CalendarDelete,
                    search_calendar, search_calendar_dte, search_finished_calendar, search_finished_calendar_dte
                    )


app_name = 'Calendar'
urlpatterns = [
    path("", CalendarListView.as_view(), name="list_calendar"),
    # path("add_calendar", CreateCalendar.as_view(), name="create_calendar"),
    path("finished_jobs", FinishedCalendarListView.as_view(), name="finished_jobs"),
    path("add_calendar/<int:machine_id>", create_calendar, name="add_calendar"),
    path('<int:calendar_id>', EditCalendar.as_view(), name='edit_calendar'),
    path('<int:calendar_id>/delete/', CalendarDelete.as_view(), name='delete_calendar'),
    path('search_calendar', search_calendar,  name='search_calendar'),
    path('search_finished_calendar', search_finished_calendar,  name='search_finished_calendar'),
    path('search_calendar_dte', search_calendar_dte,  name='search_calendar_dte'),
    path('search_finished_calendar_dte', search_finished_calendar_dte,  name='search_finished_calendar_dte'),


]
