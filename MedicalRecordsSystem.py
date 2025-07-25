from Appoinment import *

class MedicalRecordsSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}

    def add_patient(self, patient):
        self.patients[patient.id] = patient

    def add_doctor(self, doctor):
        self.doctors[doctor.id] = doctor

    def find_doctor_for_ailment(self, ailment, shift):
        ailment = ailment.lower()
        shift = shift.lower()

        for doctor in self.doctors.values():
            if doctor.ailment.lower() == ailment and doctor.shift.lower() == shift:
                return doctor

        return None

    def is_doctor_available(self, doctor, datetime):
        for patient in self.appointments.values():
            if patient.doctor.id == doctor.id and patient.datetime == datetime:
                return False
            return True

    def schedule_auto_appointment(self, appointment_id, patient_id, datetime, shift):
        patient = self.patients.get(patient_id)
        if not patient:
            raise ValueError('Patient not found')

        doctor = self.find_doctor_for_ailment(patient.aliment, shift)
        if doctor and self.is_doctor_available(doctor, datetime):
            appointment = Appointment(appointment_id, patient, doctor, datetime, patient.aliment)
            self.appointments[appointment.id] = appointment
            return appointment

        raise Exception('No appointment available')

    def get_appointments_report(self):
        return [patient.get_details() for patient in self.appointments.values()]




