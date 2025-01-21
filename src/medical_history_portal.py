from medical_history import MedicalHistory

medical_history = []

class MedicalHistoryPortal:


    def add_medicalHistory(self, name,id,Doctors_met,disease):
        new_medical_history = MedicalHistory(name,id,Doctors_met,disease)
        medical_history.append(new_medical_history)
        return f"""
        Name: {name}
        ID: {id}
        Doctors_met: {Doctors_met}
        Disease: {disease}
        """


    def find_medicalHistory(self, name):
        for medical in medical_history:
            if medical.name == name:
                return medical