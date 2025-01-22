import unittest

import doctor
from patient import Patient, book_hospital_appointment


class PatientTest(unittest.TestCase):
    def test_that_phone_number_is_not_more_than_11(self):
        patient = Patient("first_name", "last_name", "date_of_birth", "number", "street", "state", "00000000000")
        self.assertRaises(ValueError, patient.validate_phone_number,"00")

    def test_to_check_for_random_numbers(self):
        patient = Patient("first_name", "last_name", "date_of_birth", "number", "street", "state", "00000000000")
        generated_id = patient.generate_patient_id()
        self.assertEqual(len(generated_id), 13)



    def test_that_you_can_book_appointment(self):
        doc = doctor.Doctor("first_name", "last_name", "date_of_birth","00000000000", "number", "street", "state","CHEMOTHERAPIST")
        patient = Patient("first_name", "last_name", "date_of_birth", "number", "street", "state", "00000000000")

        book_hospital_appointment(patient.get_patient_id(),"first_name" , "date", "reasons")






