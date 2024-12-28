from django.urls import path
from .views import handle_car_enquiry_form, success_page

urlpatterns = [
    path('', handle_car_enquiry_form, name='car_enquiry_form'),
    path('success/', success_page, name='car_enquiry_success'),
]
