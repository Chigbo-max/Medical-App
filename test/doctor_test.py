import unittest
import doctor


class DoctorTest(unittest.TestCase):
    def test_that_phone_number_is_not_more_than_11(self):
        patient = doctor.Doctor("first_name", "last_name", "date_of_birth","00000000000", "number", "street", "state","optician")
        print(patient)