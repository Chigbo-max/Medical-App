import unittest
from patient import Patient

from medical_history_portal import MedicalHistoryPortal, medical_history


class MedicalHistoryTest(unittest.TestCase):
    def test_something(self):
        new_medical_history = MedicalHistoryPortal()

        patient1 = Patient("first_name", "last_name", "date_of_birth", "00000000000", "number",
                                                  "street", "state")

        new_medical_history.add_medicalHistory("name", patient1.get_patient_id(), "Doctors_met", "disease")
        self.assertEqual(len(medical_history), 1)

