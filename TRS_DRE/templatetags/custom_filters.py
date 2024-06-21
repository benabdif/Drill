from django import template
from datetime import datetime, date

register = template.Library()


@register.filter
def calculate_month_span(movement):
    return (
        (movement.end_date.year - movement.start_date.year) * 12
        + movement.end_date.month
        - movement.start_date.month
        + 1
    )

@register.filter
def is_past(end_date):
    if end_date and end_date < date.today():
        return True
    return False

@register.filter
def get_current_span(start_date):
    now = datetime.now().date()
    span = (now - start_date).days
    print(span)
    return (span * (200 / 30)) + 300


@register.filter
def calculate_start_month_index(movement, start_year):
    return (movement.start_date.year - start_year) * 12 + (
        movement.start_date.month - 1
    )
