import re

def validate_name(name):
    if not re.match(r'^[A-Za-z\s]+$', name):
        return "Invalid name. Only alphabetic characters and spaces are allowed."
    return None

def validate_passport_number(passport_number):
    if not re.match(r'^[A-Za-z0-9]{9}$', passport_number):
        return "Invalid passport number. It must be alphanumeric and exactly 9 characters long."
    return None

def validate_phone_number(phone_number):
    if not re.match(r'^\d{10}$', phone_number):
        return "Invalid phone number. It must be a 10-digit number."
    return None

def validate_email(email):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return "Invalid email address. Please enter a valid email."
    return None

def validate_departure_date(departure_date):
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', departure_date):
        return "Invalid departure date. It must be in the format 'dd/mm/yyyy'."
    return None

def validate_payment_method(payment_method):
    valid_payment_methods = ['credit', 'debit', 'netbanking']
    if payment_method not in valid_payment_methods:
        return "Invalid payment method. Choose either 'credit', 'debit', or 'netbanking'."
    return None

def get_booking_data():
    while True:
        name = input("Enter the traveler's name (alphabetic characters and spaces only): ")
        error = validate_name(name)
        if error:
            print(error)
            continue
        
        passport_number = input("Enter the passport number (alphanumeric and exactly 9 characters long): ")
        error = validate_passport_number(passport_number)
        if error:
            print(error)
            continue
        
        phone_number = input("Enter the phone number (10-digit number): ")
        error = validate_phone_number(phone_number)
        if error:
            print(error)
            continue
        
        email = input("Enter the email address: ")
        error = validate_email(email)
        if error:
            print(error)
            continue
        
        departure_date = input("Enter the departure date (dd/mm/yyyy): ")
        error = validate_departure_date(departure_date)
        if error:
            print(error)
            continue
        
        payment_method = input("Enter the payment method ('credit', 'debit', or 'netbanking'): ")
        error = validate_payment_method(payment_method)
        if error:
            print(error)
            continue
        
        # If all validations pass
        print("All fields are valid.")
        break


get_booking_data()
