import unittest
from registration_portal import RegistrationPortal, patient_list,doctor_list


class PatientPortalTestcase(unittest.TestCase):
    def test_to_if_you_can_save_new_patient(self):
        patient_portal = RegistrationPortal()
        patient = patient_portal.register_patient("first_name", "last_name", "date_of_birth", "00000000000", "number", "street", "state")
        self.assertEqual(len(patient_list), 1)

        doctor_portal = RegistrationPortal()
        new_doctor = doctor_portal.register_doctor("first_name", "last_name", "date_of_birth", "00000000000", "number", "street", "state","surgeon")
        self.assertEqual(len(doctor_list), 1)
