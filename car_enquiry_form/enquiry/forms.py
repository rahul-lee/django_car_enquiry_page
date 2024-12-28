from django import forms
from django.core.validators import RegexValidator


class CarEnquiryForm(forms.Form):
    CAR_BRANDS = [
        ('Tata', 'Tata'),
        ('Honda', 'Honda'),
        ('Ford', 'Ford'),
        ('Tesla', 'Tesla'),
    ]

    CAR_MODELS = [
        ('Model 2024', 'Model 2024'),
        ('Model 2023', 'Model 2023'),
        ('Model 2022', 'Model 2022'),
        ('Model 2021', 'Model 2021'),
        ('Model 2020', 'Model 2020'),
    ]
    
    CAR_YEARS = [(str(year), str(year)) for year in range(2020, 2025)]
    
    CAR_VARIANTS = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
    ]
    
    CITIES = [
        ('Chennai', 'Chennai'),
        ('Delhi', 'Delhi'),
        ('Bangalore', 'Bangalore'),
    ]
    
    STATES = [
        ('TamilNadu', 'TamilNadu'),
        ('Karnataka', 'Karnataka'),
        ('Delhi', 'Delhi'),
    ]

    car_brand = forms.ChoiceField(choices=CAR_BRANDS, required=True, label="Car Brand")
    car_model = forms.ChoiceField(choices=CAR_MODELS, required=True, label="Car Model")
    car_year = forms.ChoiceField(choices=CAR_YEARS, required=True, label="Car Year")
    car_variant = forms.ChoiceField(choices=CAR_VARIANTS, required=True, label="Car Variant")
    city = forms.ChoiceField(choices=CITIES, required=True, label="City")
    state = forms.ChoiceField(choices=STATES, required=True, label="State")
    first_name = forms.CharField(max_length=100, required=True, label="First Name")
    last_name = forms.CharField(max_length=100, required=False, label="Last Name")
    
    mobile_number = forms.CharField(
        max_length=10, 
        min_length=10, 
        required=True, 
        label="Mobile Number",
        validators=[RegexValidator(r'^\d{10}$', 'Mobile number must be a Number and exactly 10 digits.')],
        error_messages={
            'required': 'Please enter your mobile number.',
            'max_length': 'Mobile number cannot be longer than 10 digits.',
            'min_length': 'Mobile number cannot be shorter than 10 digits.',
        }
    )

    email = forms.EmailField(required=False, label="Email Address")
    preferred_contact_method = forms.ChoiceField(
        choices=[('Phone', 'Phone'), ('Email', 'Email'), ('Both', 'Both')], required=True, label="Preferred Contact Method")
    enquiry_message = forms.CharField(widget=forms.Textarea, required=False, label="Enquiry Message")
    test_drive_request = forms.BooleanField(required=False, label="Request a Test Drive")
