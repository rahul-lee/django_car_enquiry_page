# Car Enquiry Form

A Django-based web application for managing car enquiries, where users can fill out a form to submit details about their car preferences, personal information, and request a test drive. The application saves all enquiry data into an Excel file.

## Features

- Fully functional car enquiry form with the following fields:
  - Car Brand
  - Car Model
  - Car Year
  - Car Variant
  - City
  - State
  - First Name
  - Last Name
  - Mobile Number
  - Email Address
  - Preferred Contact Method
  - Enquiry Message
  - Test Drive Request
- Data validation for required fields and proper formatting (e.g., mobile number validation).
- Form submission success page.
- Saves all enquiry data into an Excel file.

## Prerequisites

- Python 3.8+
- Django 5.1.4
- OpenPyXL library for handling Excel files

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/car-enquiry-form.git
   cd car-enquiry-form
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the project:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## File Structure

```
car_enquiry_form/
├── car_enquiry_form/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── enquiry/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── car_enquiry_form.html
│       └── success.html
├── manage.py
├── requirements.txt
└── README.md
```

## Usage

1. Navigate to the root URL to view the car enquiry form.
2. Fill out the form with the required details.
3. Submit the form to save the data into an Excel file (`car_enquiry_data.xlsx`).
4. A success page will confirm submission.

## Technologies Used

- **Backend:** Django 5.1.4
- **Frontend:** HTML, CSS, JavaScript (for form styling and validation)
- **Excel Handling:** OpenPyXL

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Developed by [rahul-lee](https://github.com/rahul-lee).

Feel free to contribute or report issues!
