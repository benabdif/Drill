

# from django.shortcuts import render
# from .models import Rigg, Movementg
# from datetime import date

# def get_month_span(start_date, end_date):
#     """Calculate the number of months between two dates, inclusive."""
#     start_month = start_date.month
#     end_month = end_date.month
#     year_span = end_date.year - start_date.year
#     month_span = end_month - start_month + 1 + (year_span * 12)
#     return month_span

# def rig_timeline1(request):
#     rigs = Rigg.objects.all()
#     movements = Movementg.objects.all().order_by('start_date')

#     # Define the list of months for display
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#     # Define a range of years you want to cover
#     years = list(range(2024, 2027))  # Adjust the range as necessary

#     # Prepare the data for rendering
#     movement_spans = []
#     for movement in movements:
#         month_span = get_month_span(movement.start_date, movement.end_date)
#         movement_spans.append({
#             'rig': movement.rig,
#             'well': movement.well,
#             'start_date': movement.start_date,
#             'end_date': movement.end_date,
#             'month_span': month_span,
#             'start_month': movement.start_date.month,
#             'start_year': movement.start_date.year,
#             'end_year': movement.end_date.year
#         })
#         print("=" * 33)
#         print(month_span)
#         for year in years:
#             print(year)

#     context = {
#         'rigs': rigs,
#         'movements': movement_spans,
#         'months': months,
#         'years': years
#     }
        

        

#     return render(request, 'blog/rig_timeline1.html', context)
