from django import template
from datetime import datetime, date

register = template.Library()


@register.filter
def calculate_month_span(movement):
    start_date = movement.start_date
    end_date = movement.end_date

    # Calculate the number of days between the two dates
    delta = end_date - start_date
    
    return delta.days * (200 / 30)

@register.filter
def is_past(end_date):
    if end_date and end_date < date.today():
        return True
    return False

@register.filter
def get_current_span(start_date):
    now = datetime.now().date()
    span = (now - start_date.replace(month=1, day=1)).days
    return (span * (2400 / 365.24)) + 300


@register.filter
def calculate_start_month_index(movement, start_year):
    start_date = movement.start_date
    start_year_date = datetime(year=start_year, month=1, day=1).date()
    
    # Calculate the number of days between the two dates
    delta = start_date - start_year_date
    
    return delta.days * ((2400 / 365.24 ))
