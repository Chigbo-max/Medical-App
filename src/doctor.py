
from patient import Patient

class Doctor(Patient):
    def __init__(self, first_name, last_name, date_of_birth, phone_number, number, street, state, specialization=""):
        super().__init__(first_name, last_name, date_of_birth, phone_number, number, street, state)
        self.specialization = self.spec_check(specialization.upper())

    def spec_check(self, specialization):
        list_of_specs = ["SURGEON", "MIDWIVES", "GENERAL", "CHEMOTHERAPIST", "DENTIST", "PSYCHOTHERAPIST", "OPTICIANS","PHYSIOTHERAPIST", "ONCOLOGIST"]
        for specName in list_of_specs:
            if specialization == specName:
                return specialization
            else:
                raise ValueError("Specialist Not Available")