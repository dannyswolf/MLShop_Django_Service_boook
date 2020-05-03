from datetime import datetime, timedelta
from calendar import HTMLCalendar, LocaleHTMLCalendar
from .models import Calendar


# Αλλαγή μηνών απο αγγλικα σε ελληνικά
enu_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
              'October',
              'November', 'December']
greek_months = ['Ιανουάριος', 'Φεβρουάριος', 'Μάρτιος', 'Απρίλιος', 'Μάιος', 'Ιούνιος', 'Ιούλιος',
                'Αύγουστος',
                'Σεπτέμβριος', 'Οκτώβριος', 'Νοέμβριος', 'Δεκέμβριος']



# Αλλαγή days name  απο αγγλικα σε ελληνικά
enu_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

greek_days = ['Δευτέρα', 'Τρίτη', 'Τετάρτη', 'Πέμπτη', 'Παρασκευή', 'Σάββατο', 'Κυρικακή']


class MyHtmlCalendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        self.data = Calendar.objects.all().filter(Κατάσταση=True)
        # ----Sorting----
        self.dict_services = self.data.values()
        self.sorted_data = sorted(self.dict_services, key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"), reverse=True)
        super(MyHtmlCalendar, self).__init__()
    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):

        d = ''

        for event in self.sorted_data:

            Ημερομηνία = event['Ημερομηνία']
            old_date = datetime.strptime(Ημερομηνία, "%d/%m/%Y")
            task_month = old_date.month
            task_day = old_date.day
            if self.month == task_month and task_day == day:

                d += f'<li><a class="btn btn-primary" role="button" href="' f'{event["id"]}"> {event["Πελάτης"]}</a></li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month

    # formatmonth(theyear, themonth, withyear=True)
    def formatmonth(self, withyear=True):

        events = self.sorted_data

        cal = f'<table border="1" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        for month in range(1, 13):
            # Αλλαγή μηνών απο αγγλικα σε ελληνικά
            if enu_months[month - 1] in cal:

                html_cal = cal.replace(enu_months[month - 1], greek_months[month - 1])
        for day in range(7):
            if enu_days[day] in html_cal:

                html_cal = html_cal.replace(enu_days[day], greek_days[day])

        return html_cal


class MyFinishedHtmlCalendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        self.data = Calendar.objects.all().filter(Κατάσταση=False)
        # ----Sorting----
        self.dict_services = self.data.values()
        self.sorted_data = sorted(self.dict_services, key=lambda x: datetime.strptime(x['Ημερομηνία'], "%d/%m/%Y"),
                                  reverse=True)

        super(MyFinishedHtmlCalendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):

        d = ''

        for event in self.sorted_data:

            Ημερομηνία = event['Ημερομηνία']
            old_date = datetime.strptime(Ημερομηνία, "%d/%m/%Y")

            task_month = old_date.month
            task_day = old_date.day
            if self.month == task_month and task_day == day:
                d += f'<li><a class="btn btn-primary" role="button" href="' f'{event["id"]}"> {event["Πελάτης"]}</a></li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month

    # formatmonth(theyear, themonth, withyear=True)
    def formatmonth(self, withyear=True):

        events = self.sorted_data

        cal = f'<table border="1" cellpadding="0" cellspacing="0"  class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        for month in range(1, 13):
            # Αλλαγή μηνών απο αγγλικα σε ελληνικά
            if enu_months[month - 1] in cal:
                html_cal = cal.replace(enu_months[month - 1], greek_months[month - 1])
        for day in range(7):
            if enu_days[day] in html_cal:
                html_cal = html_cal.replace(enu_days[day], greek_days[day])

        return html_cal
