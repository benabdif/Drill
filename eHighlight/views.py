from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import loader
import io
import openpyxl
from .forms import eHighlightRecordForm  # Assuming you have a form for the model
from .models import eHighlight_Record
from django.db.models import Sum, Avg, Count
import locale
from collections import defaultdict
from datetime import datetime
from django.db.models.functions import TruncMonth

# Your view code here


def eHighlight_Re(request):
    REC = eHighlight_Record.objects.all()
    context = { "REC": REC }
    return render(request, "blog/eHighlight.html", context)

def basec(request):
    return render(request, 'blog/base_generic.html')



class eHighlightRecordListView(ListView):
    model = eHighlight_Record
    template_name = 'blog/eHighlight_Record_list.html'
    context_object_name = 'records'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Unit counts
        sacu_1_count = eHighlight_Record.objects.filter(unit='SACU 1').count()
        sacu_2_count = eHighlight_Record.objects.filter(unit='SACU 2').count()
        sacu_3_count = eHighlight_Record.objects.filter(unit='SACU 3').count()
        HSE_Group = eHighlight_Record.objects.filter(unit='HSE Group').count()
        Dispatcher_Group = eHighlight_Record.objects.filter(unit='Dispatcher Group').count()
        Surveyor_Group = eHighlight_Record.objects.filter(unit='Surveyor Group').count()
        Waste_Management_Group = eHighlight_Record.objects.filter(unit='Waste Management Group').count()
        Engineering_Support = eHighlight_Record.objects.filter(unit='Engineering Support').count()
        all_records_count = eHighlight_Record.objects.count()

        context['sacu_1_count'] = sacu_1_count
        context['sacu_2_count'] = sacu_2_count
        context['sacu_3_count'] = sacu_3_count
        context['HSE_Group'] = HSE_Group
        context['Dispatcher_Group'] = Dispatcher_Group
        context['Surveyor_Group'] = Surveyor_Group
        context['Waste_Management_Group'] = Waste_Management_Group
        context['Engineering_Support'] = Engineering_Support
        context['all_records_count'] = all_records_count  # This code for count all_Ehiglight

        # Monthly counts
        monthly_counts = (eHighlight_Record.objects
                          .filter(date__isnull=False)
                          .annotate(month=TruncMonth('date'))
                          .values('month')
                          .annotate(count=Count('id'))
                          .order_by('month'))

        # Initialize the dictionary with all months set to 0
        month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        monthly_count_dict = {month: 0 for month in month_order}

        # Update the dictionary with actual counts
        for entry in monthly_counts:
            month_name = entry['month'].strftime('%B')
            monthly_count_dict[month_name] += entry['count']

        context['monthly_counts'] = monthly_count_dict

        # Print counts
        for x, y in context['monthly_counts'].items():
            print(y)

        # Sorting the dictionary by month order
        sorted_month_dict = {month: context['monthly_counts'][month] for month in month_order}

        print("Dictionary sorted by months:")
        print(sorted_month_dict)

                

        return context
            
 


class eHighlightRecordDetailView(DetailView):
    model = eHighlight_Record
    template_name = 'blog/eHighlight_Record_detail.html'
    context_object_name = 'record'

class eHighlightRecordCreateView(CreateView):
    model = eHighlight_Record
    form_class = eHighlightRecordForm
    template_name = 'blog/eHighlight_Record_form.html'
    success_url = reverse_lazy('eHighlight_Record_list')

# Update_View
class eHighlightRecordUpdateView(UpdateView):
    model = eHighlight_Record
    form_class = eHighlightRecordForm
    template_name = 'blog/eHighlight_Record_form.html'
    success_url = reverse_lazy('eHighlight_Record_list')


# Delete_View
class eHighlightRecordDeleteView(DeleteView):
    model = eHighlight_Record
    template_name = 'blog/eHighlight_Record_confirm_delete.html'
    success_url = reverse_lazy('eHighlight_Record_list')

# Function-based view to handle other custom logic if needed
def custom_view(request):
    # Add your custom logic here
    return render(request, 'blog/custom_template.html')


# Excel sheet dowenlode
def download_records_excel(request):
    # Create an in-memory output file for the new workbook.
    output = io.BytesIO()

    # Create a workbook and add a worksheet.
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "eHighlight Records"

    # Define the column headers
    headers = ["#", "Date", "Week", "Cost", "Unit", "Highlight Type", "Wellsite Activity", "Document", "Image", "Details"]
    ws.append(headers)

    # Fetch the records and write to the worksheet
    records = eHighlight_Record.objects.all()
    
    for idx, record in enumerate(records, start=1):
        ws.append([
            idx,
            record.date,
            record.week,
            record.Cost,
            record.unit,
            record.highlight_type,
            record.wellsite_activity,
            record.document.url if record.document else "No Document",
            record.image.url if record.image else "No Image",
            f"Details URL: /url/to/details/{record.pk}"
        ])

    # Save the workbook to the in-memory file
    wb.save(output)
    output.seek(0)

    # Set up the HTTP response with the Excel file
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=eHighlight_Records.xlsx'

    return response






def introduce(request):
    all_apps = 'Fadhel'
    return render(request, 'blog/introduce.html', {'all_apps': all_apps})



def All_Apps(request):
    rec = eHighlight_Record.objects.all()
    All_apps = 'Fadhel'
    return render(request, 'blog/apps.html', {'rec': rec, 'All_apps':All_apps})


def total_cost_view(request):
    # total_cost = eHighlight_Record.objects.aggregate(total_cost=Sum('Cost'))['total_cost']
    info = eHighlight_Record.objects.all()
    return render(request, 'blog/total_cost.html', {'info':info })
    # return render(request, 'total_cost.html', {'total_cost': total_cost})




def test(request):
    mydata = eHighlight_Record.objects.all().order_by('Cost').values()
    template = loader.get_template('total_cost.html')
    context = {
        'mydata': mydata,
    }
    return HttpResponse(template.render(context, request))

