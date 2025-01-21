import unittest
from patient import Patient


class PatientTest(unittest.TestCase):
    def test_that_phone_number_is_not_more_than_11(self):
        patient = Patient("first_name", "last_name", "date_of_birth","00000000000", "number", "street", "state")
        self.assertRaises(ValueError, patient.validate_phone_number,"00")

    def test_to_check_for_random_numbers(self):
        patient = Patient("first_name", "last_name", "date_of_birth","00000000000", "number", "street", "state")
        generated_id = patient.generate_patient_id()
        self.assertEqual(len(generated_id), 13)





