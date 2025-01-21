import random
from address import Address

class Patient:


    def __init__(self, first_name, last_name, date_of_birth, phone_number, number, street, state):
        self.verify_name(first_name, last_name)
        self.date_of_birth = date_of_birth
        self.validate_phone_number(phone_number)
        self.address = Address(number, street, state)
        self.__patient_id = self.generate_patient_id()


    def validate_phone_number(self, phone_number):
        if len(phone_number) == 11:
            self.phone_number = phone_number
        else:
            raise ValueError("Phone number must be 11 digits")



    def get_patient_id(self):
        return self.__patient_id

    def verify_name(self,first_name, last_name):
        if first_name == "" or last_name == "":
            raise ValueError("First name and last name cannot be empty")
        self.first_name = first_name
        self.last_name = last_name

    def generate_patient_id(self):
        initial_string = "PAT"
        for count in range(1):
            random_number = random.randint(1000000000, 9999999999)
            initial_string = initial_string + str(random_number)
        return initial_string


    def __str__(self):
       return  f"""
        Name: {self.first_name} {self.last_name}
        D.O.B: {self.date_of_birth}
        Contact Details: {self.phone_number}
        Patient ID: {self.patient_id}
        """

    def book_hospital_appointment (self):
        pass
