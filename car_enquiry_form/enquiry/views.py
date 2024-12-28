from django.shortcuts import render, redirect
from .forms import CarEnquiryForm
import openpyxl
import os

EXCEL_FILE = "car_enquiry_data.xlsx"

if not os.path.exists(EXCEL_FILE):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Car Enquiries"
    sheet.append([
        "Car Brand", "Car Model", "Car Year", "Car Variant", "City", "State",
        "First Name", "Last Name", "Mobile Number", "Email", "Preferred Contact Method",
        "Enquiry Message", "Test Drive Request"
    ])
    wb.save(EXCEL_FILE)


def handle_car_enquiry_form(request):
    if request.method == 'POST':
        form = CarEnquiryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            wb = openpyxl.load_workbook(EXCEL_FILE)
            sheet = wb.active
            sheet.append([
                data['car_brand'], data['car_model'], data['car_year'], data['car_variant'],
                data['city'], data['state'], data['first_name'], data['last_name'] or "",
                data['mobile_number'], data['email'] or "", data['preferred_contact_method'],
                data['enquiry_message'] or "", data['test_drive_request']
            ])
            wb.save(EXCEL_FILE)

            return redirect('car_enquiry_success')

    else:
        form = CarEnquiryForm()

    return render(request, 'car_enquiry_form.html', {'form': form})


def success_page(request):
    return render(request, 'success.html')
