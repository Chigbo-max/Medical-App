import random
import appointments
from address import Address

appointment_list = []


def display_appointment_list():
    for appointment in appointment_list:
        print(appointment)


def book_hospital_appointment(patient_id, doctors_name, date, reasons):
    from registration_portal import find_doctor
    appointment_booking = appointments.Appointment(patient_id, doctors_name, date, reasons)
    if find_doctor(doctors_name):
        appointment_list.append(appointment_booking)
        print("Appointment successfully booked.")
    else:
        raise ValueError(f"Doctor {doctors_name} not found.")


class Patient:

    def __init__(self, first_name, last_name, date_of_birth, number, street, state, phone_number="N/A"):
        self.verify_name(first_name, last_name)
        self.date_of_birth = date_of_birth
        self.validate_phone_number(phone_number)
        self.address = Address(number, street, state)
        self.__patient_id = ""
        if self.__patient_id == "":
            self.generate_patient_id()

    def validate_phone_number(self, phone_number):
        if len(phone_number) == 11:
            self.phone_number = phone_number
        else:
            raise ValueError("Phone number must be 11 digits")

    def get_patient_id(self):
        return self.__patient_id

    def verify_name(self, first_name, last_name):
        if first_name == "" or last_name == "":
            raise ValueError("First name and last name cannot be empty")
        self.first_name = first_name
        self.last_name = last_name

    def generate_patient_id(self):
        initial_string = "PAT"
        random_number = random.randint(1000000000, 9999999999)
        self.__patient_id = initial_string + str(random_number)


    def __str__(self):
        return f"""
        Name: {self.first_name} {self.last_name}
        D.O.B: {self.date_of_birth}
        Contact Details: {self.phone_number}
        Patient ID: {self.__patient_id}
        """
