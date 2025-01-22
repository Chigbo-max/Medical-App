import random
from patient import Patient

class Doctor(Patient):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, number, street, state, specialization=""):
        super().__init__(first_name, last_name, date_of_birth, number, street, state, phone_number)
        self.specialization = self.spec_check(specialization)
        self.is_booked = False
        self.bookings = 0

    def generate_doctor_id(self):
        initial_string = "DOC"
        random_number = random.randint(1000000000, 9999999999)
        self.__patient_id = initial_string + str(random_number)

    def spec_check(self, specialization):
        list_of_specs = ["SURGEON", "MIDWIVES", "GENERAL", "CHEMOTHERAPIST", "DENTIST", "PSYCHOTHERAPIST", "OPTICIANS", "PHYSIOTHERAPIST", "ONCOLOGIST"]
        specialization = specialization.upper()
        if specialization in list_of_specs:
            return specialization
        else:
            raise ValueError(f"Specialist Not Available. Available specializations are: {', '.join(list_of_specs)}")

    @classmethod
    def booked(cls):
        cls.is_booked = True

    @classmethod
    def check_if_booked(cls):
        return cls.is_booked
