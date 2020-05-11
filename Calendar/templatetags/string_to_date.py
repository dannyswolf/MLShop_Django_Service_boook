from django import template
from django.template.defaultfilters import stringfilter
import datetime

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def string_to_timestamp(value):
    try:
    # int(datetime.datetime.strptime('01/12/2011', '%d/%m/%Y').strftime("%s"))
        return int(datetime.datetime.strptime(value, "%d/%m/%Y").strftime("%s"))
    except ValueError:  # Οταν δέν έχουμε ημερομηνία
        return 1

