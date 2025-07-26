import unittest
from medical_system import MedicalSystem
from patient import Patient
from doctor import Doctor

class TestMedicalSystem(unittest.TestCase):

    def setUp(self):
        self.system = MedicalSystem()
        self.new_doc = Doctor("Dr. Will", "Dermatology", {"phone": "123456789", "email": "will@gmail.com", "home address": "2, broad street", "gender": "Male"})
        self.new_patient = Patient("Ade", "10/10/1995 03:00", "Skin rash", "Dermatology", {"phone": "123456789", "gender": "female", "address": "12 broad way", "email": "ade@gmail.com"})

    def test_that_medical_system_can_add_patient(self):
        self.system.add_patient(self.new_patient)
        self.assertEqual(self.system.find_patient_record(self.new_patient.get_id), str(self.new_patient))

    def test_that_medical_system_cannot_add_same_patient_id(self):
        self.system.add_patient(self.new_patient)
        self.assertRaises(ValueError, self.system.add_patient, self.new_patient)

    def test_that_medical_system_cannot_add_patient_with_future_dob(self):
        wrong_patient = Patient("ada", "01/01/2026", "Skin disease", "Dermatology", {"phone": "123456789", "gender": "female", "address": "12 broad lane", "email": "ada@gamil.com"})
        self.assertRaises(ValueError, self.system.add_patient, wrong_patient)


    def test_that_medical_system_cannot_add_patient_with_dob_format(self):
        wrong_dob = Patient("ify", "2000/03/23", "skin", "Dermatology", {"phone": "123456789", "gender": "female", "address": "12 broad way", "email": "ade@gmail.com"})
        self.assertRaises(ValueError, self.system.add_patient, wrong_dob)


    def test_that_medical_system_cannot_add_patient_with_no_info(self):
        no_name = Patient("", "10/05/1996", "skin", "Dermatology", {})
        self.assertRaises(ValueError, self.system.add_patient, no_name)

        no_problem = Patient('olu', '10/05/2000', '', 'Dermatology', {})
        self.assertRaises(ValueError, self.system.add_patient, no_problem)

        no_speciality = Patient('ade', '10/05/2000', 'cough', '', {})
        self.assertRaises(ValueError, self.system.add_patient, no_speciality)


    def test_that_medical_system_can_add_doctor(self):
        self.system.add_doctor(self.new_doc)
        self.assertEqual(self.system.find_doctor_record(self.new_doc.get_id), str(self.new_doc))


    def test_that_medical_system_cannot_add_same_doctor_id(self):
        self.system.add_doctor(self.new_doc)
        self.assertRaises(ValueError, self.system.add_doctor, self.new_doc)


    def test_that_medical_system_cannot_add_doctor_with_no_info(self):
        no_name = Doctor("", "Cardiology", {})
        self.assertRaises(ValueError, self.system.add_doctor, no_name)

        no_specialty = Doctor('Dr. Will', '', {})
        self.assertRaises(ValueError, self.system.add_doctor, no_specialty)


    def test_that_medical_system_can_assign_doctor_to_patient(self):
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        result = self.system.assign_doctor_to_patient(self.new_patient, "25/08/2025 03:00")
        self.assertIn("Appointment has been scheduled for patient Ade", result)


    def test_that_medical_system_cannot_find_doctor(self):
        another_patient = Patient('Ice', '10/01/1995 02:00', 'toothache', 'Dentistry', {'phone number': '0000000000', 'email': 'ice@email.com', 'home address': 'Den close'})
        self.system.add_patient(another_patient)
        self.system.add_doctor(self.new_doc)
        result = self.system.assign_doctor_to_patient(another_patient, "25/08/2025 02:00")
        self.assertIn("No doctor available for this patient", result)



    def test_that_medical_system_can_cancel_appointment(self):
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        appointment_date = "25/08/2025 03:00"
        self.system.assign_doctor_to_patient(self.new_patient, appointment_date)

        cancel_result = self.system.cancel_appointment(self.new_patient.get_id, appointment_date)
        self.assertIn("Appointment for patient Ade on 25/08/2025 03:00 has been cancelled", cancel_result)

        result = self.system.get_appointment(self.new_patient.get_id)
        self.assertEqual(result, "No appointments found for this patient")

    def test_that_medical_system_cannot_cancel_appointment_without_booking(self):
        result = self.system.cancel_appointment("", "25/08/2025 03:00")
        self.assertIn("No appointment scheduled for this patient", result)

    def test_that_medical_system_can_reschedule_appointment(self):
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        self.system.assign_doctor_to_patient(self.new_patient, '27/07/2025 14:00')
        result = self.system.reschedule_appointment(self.new_patient.get_id, '27/07/2025 14:00','30/07/2025 11:30')
        self.assertIn("has been rescheduled", result)

    def test_that_medical_system_cannot_reschedule_appointment(self):
        self.assertRaises(ValueError, self.system.reschedule_appointment, "", "01/01/2024 10:00", "02/01/2024 11:00")

    def test_that_medical_system_cannot_reschedule_with_wrong_date(self):
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        self.assertRaises(ValueError, self.system.reschedule_appointment, self.new_patient.get_id, "01/01/2024 10:00", "02/01/2024 11:00")

    def test_that_medical_record_can_get_appointment(self):
        self.system.add_patient(self.new_patient)
        self.system.add_doctor(self.new_doc)
        self.system.assign_doctor_to_patient(self.new_patient, '27/07/2025 14:00')
        result = self.system.get_appointment(self.new_patient.get_id)
        self.assertIn("Appointment", result)


    def test_that_medical_system_cannot_get_appointment_without_booking(self):
        result = self.system.get_appointment("")
        self.assertEqual(result, "No appointments found for this patient")


    def test_that_medical_system_can_find_patient_record(self):
        self.assertRaises(ValueError, self.system.find_patient_record, self.new_patient.get_id)


    def test_that_medical_system_can_find_doctor_record(self):
        self.assertRaises(ValueError, self.system.find_doctor_record, self.new_doc.get_id)


