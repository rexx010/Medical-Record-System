from datetime import datetime
from appointment import Appointment
from doctor import Doctor
from patient import Patient


class MedicalSystem:
    def __init__(self):
        self.__patient_records = {}
        self.__doctor_records = {}
        self.__appointments = []

    def add_patient(self, patient):
        if patient.get_id in self.__patient_records:
            raise ValueError("Patient already registered")

        if not patient.name:
            raise ValueError('Patient name cannot be empty')
        try:
            dob = datetime.strptime(patient.dob, '%d/%m/%Y %H:%M')
        except ValueError:
            raise ValueError("Date of birth must be in DD/MM/YYYY HH:MM format(eg, 10/05/2000 02:00)")

        if dob > datetime.today():
            raise ValueError("Date of birth cannot be in the future")

        if not patient.problem:
            raise ValueError('Patient problem cannot be empty')

        if not patient.speciality_needed:
            raise ValueError('Speciality cannot be empty')

        self.__patient_records[patient.get_id] = patient

    def add_doctor(self, new_doctor: Doctor):
        if new_doctor.get_id in self.__doctor_records:
            raise ValueError('Doctor already registered')

        if not new_doctor.name:
            raise ValueError('Doctor name cannot be empty')

        if not new_doctor.specialisation:
            raise ValueError('Doctor specialisation cannot be empty')

        self.__doctor_records[new_doctor.get_id] = new_doctor


    def assign_doctor_to_patient(self, patient: Patient, date: str):
        try:
            new_date = datetime.strptime(date, '%d/%m/%Y %H:%M')
        except ValueError:
            raise ValueError("Appointment date must be in DD/MM/YYYY HH:MM format(eg, 10/05/2000 03:00)")

        if new_date < datetime.today():
            raise ValueError("Appointment date cannot be in the past")

        for doctor in self.__doctor_records.values():
            if patient.speciality_needed == doctor.specialisation:
                new_appointment = Appointment(patient, doctor, date)
                self.__appointments.append(new_appointment)
                return f"Appointment has been scheduled for patient {patient.name} at {new_date.strftime('%d/%m/%Y %H:%M')}"

        return f"No doctor available for this patient"


    def view_all_appointments(self):
        print("Scheduled appointments:")
        for appointment in self.__appointments:
            print(appointment)

        if not self.__appointments:
            print("No appointments scheduled.")


    def cancel_appointment(self, patient_id: str, date: str):
        try:
            cancel_date = datetime.strptime(date, '%d/%m/%Y %H:%M')
        except ValueError:
            raise ValueError("Appointment date must be in DD/MM/YYYY HH:MM format")

        for appointment in self.__appointments:
            if appointment.patient.get_id == patient_id and appointment.date == cancel_date:
                self.__appointments.remove(appointment)
                return f"Appointment for patient {appointment.patient.name} on {date} has been cancelled"
        return "No appointment scheduled for this patient"

    def reschedule_appointment(self, patient_id: str, old_date: str, new_date: str):
        try:
            date_old = datetime.strptime(old_date, '%d/%m/%Y %H:%M')
            date_new = datetime.strptime(new_date, '%d/%m/%Y %H:%M')
        except ValueError:
                raise ValueError("New appointment date must be in DD/MM/YYYY HH:MM format")
        if date_new < datetime.today():
            raise ValueError("New appointment date cannot be in the past")

        if not patient_id:
            raise ValueError("Patient id cannot be empty")

        if not old_date:
            raise ValueError("Old date cannot be empty")

        if not new_date:
            raise ValueError("New date cannot be empty")

        for appointment in self.__appointments:
            if appointment.patient.get_id == patient_id and appointment.date == date_old:
                appointment.date = date_new
                return f"Appointment for {appointment.patient.name} has been rescheduled to {new_date}"
        raise ValueError("No appointment scheduled for this patient")


    def get_appointment(self, patient_id: str):
        for appointment in self.__appointments:
            if appointment.patient.get_id == patient_id:
                return str(appointment)

        return "No appointments found for this patient"


    def find_patient_record(self, patient_id):
        for ID, patient in self.__patient_records.items():
            if ID == patient_id:
                return str(patient)
        raise ValueError("Patient not found.")


    def find_doctor_record(self, doctor_id):
        for ID, doctor in self.__doctor_records.items():
            if ID == doctor_id:
                return str(doctor)
        raise ValueError("Doctor not found.")
