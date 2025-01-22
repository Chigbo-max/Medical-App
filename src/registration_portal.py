patient_list = []
doctor_list = []

def find_doctor(name=""):
    for doc in doctor_list:
        if doc.first_name == name or doc.last_name == name:
            return doc
    raise ValueError("Doctor name doesn't match")

def find_patient(ID):
    for patient in patient_list:
        if patient.get_patient_id() == ID:
            return patient
    raise ValueError("Patient ID doesn't match")

class RegistrationPortal:

    def register_patient(self, first_name, last_name, date_of_birth, phone_number, number, street, state):
        from patient import Patient
        new_patient = Patient(first_name, last_name, date_of_birth, number, street, state, phone_number)
        patient_list.append(new_patient)

    def register_doctor(self, first_name, last_name, date_of_birth, phone_number, number, street, state, specialization):
        from doctor import Doctor
        new_doctor = Doctor(first_name, last_name, date_of_birth, phone_number, number, street, state, specialization)
        doctor_list.append(new_doctor)
