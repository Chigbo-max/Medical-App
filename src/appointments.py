import random

import registration_portal
from registration_portal import find_doctor


class Appointment:
    def __init__(self,patient_id="", doctors_name="", date="", reasons ="Not given"):
        self.reasons = reasons
        self.patient_id = registration_portal.find_patient(patient_id)
        self.doctors_name = find_doctor(doctors_name)
        self.date = date
        self.appointment_id = self.generate_appointmentId()

    def __str__(self):
        return f"""
                Appointment ID :{self.appointment_id}
                Patient ID: {self.patient_id}
                Doctors Name: {self.doctors_name}
                Date: {self.date}
                reasons: {self.reasons}
                  """

    def generate_appointmentId(self):
        initial_string = "ABK"
        for count in range(1):
            random_number = random.randint(1000000000, 9999999999)
            initial_string = initial_string + str(random_number)
        return initial_string


