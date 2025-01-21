from patient import Patient
import doctor
patient_list = []
doctor_list = []
class RegistrationPortal:

    def register_patient(self, first_name, last_name, date_of_birth, phone_number, number, street, state):
        new_patient = Patient(first_name, last_name, date_of_birth, phone_number, number, street, state)
        patient_list.append(new_patient)

    def register_doctor(self, first_name, last_name, date_of_birth, phone_number, number, street, state,specialization):
        new_doctor = doctor.Doctor(first_name, last_name, date_of_birth, phone_number, number, street, state, specialization)
        doctor_list.append(new_doctor)

