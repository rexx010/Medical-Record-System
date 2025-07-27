import re
import random
from datetime import datetime, timedelta
from medical_system import MedicalSystem
from doctor import Doctor
from patient import Patient
medical_sys = MedicalSystem()
patient_list = {}

message = """
Welcome to Medical System
=========================
press 1 to Add a Doctor
press 2 to Add a Patient
press 3 to Create Appointment
press 4 to View all Appointments
press 5 to cancel Appointment
press 6 to Reschedule Appointment
press 7 to get Appointments
press 8 to find Doctor Records
press 9 to find Patient Records
"""

while True:
    print(message)
    user_input = input()
    print()
    match user_input:
        case "1":
            print("Add Doctor")
            while True:
                try:
                    contact_info = {}
                    name = input("Enter Doctor's full Name: ").strip()
                    specialisation = input("Enter Doctor's Specialisation: ").strip()
                    phone = input("Enter Doctor's Phone Number: ").strip()
                    email = input("Enter Doctor's Email Address: ").strip()
                    address = input("Enter Doctor's Address: ").strip()
                    contact_info["phone"] = phone
                    contact_info["email"] = email
                    contact_info["address"] = address
                    doctor = Doctor(name=name, specialisation=specialisation, contact_info=contact_info)
                    medical_sys.add_doctor(doctor)
                    print(doctor)
                    break
                except ValueError:
                    print("Try again.\n")
        case "2":
            print("Add Patient")
            while True:
                try:
                    contact_info = {}
                    p_name = input("Enter Patient's Full Name: ").strip()
                    date_of_birth = input("Enter Patient's Date of Birth(DD/MM/YYYY): ").strip()
                    try:
                        date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
                        dob = date_of_birth.strftime('%d/%m/%Y')
                    except ValueError:
                        raise ValueError("Date of birth must be in DD/MM/YYYY format(eg, 10/05/2000)")
                    problem = input("Enter the patient problem: ").strip()
                    specialty_needed = input("Enter the patient specialty needed: ").strip()
                    phone = input("Enter Patient's Phone Number: ").strip()
                    email = input("Enter Patient's Email Address: ").strip()
                    address = input("Enter Patient's Address: ").strip()
                    contact_info["phone"] = phone
                    contact_info["email"] = email
                    contact_info["address"] = address
                    new_patient = Patient(name=p_name, dob=dob, problem=problem, speciality_needed=specialty_needed, contact_info=contact_info)
                    medical_sys.add_patient(new_patient)
                    patient_list[new_patient.get_id] = new_patient
                    print(new_patient)
                    break
                except ValueError:
                    print("Try again.\n")


        case "3":
            print("Create Appointment")
            while True:
                try:
                    pid = input("Enter Patient ID: ").strip()
                    schedule_date = input(
                        "Enter Appointment date in DD/MM/YYYY HH:MM format(eg, 10/05/2000 03:00): ").strip()
                    patient = patient_list.get(pid)
                    if patient:
                        result = medical_sys.assign_doctor_to_patient(patient, schedule_date)
                        print(result)
                    else:
                        print("Patient not found.")
                    break
                except ValueError:
                    print("Try again.\n")

        case "4":
            print("View all Appointments")
            medical_sys.view_all_appointments()

        case "5":
            print("Cancel Appointment")
            try:
                pid = input("Enter Patient ID: ").strip()
                date = input("Enter Appointment date in DD/MM/YYYY HH:MM format: ").strip()
                result = medical_sys.cancel_appointment(pid, date)
                print(result)
            except ValueError:
                print("Try again.\n")

        case "6":
            print("Reschedule Appointment")
            try:
                pid = input("Enter Patient ID: ").strip()
                old_date = input("Enter old Appointment date in DD/MM/YYYY HH:MM format: ").strip()
                new_date = input("Enter new Appointment date in DD/MM/YYYY HH:MM format: ").strip()
                result = medical_sys.reschedule_appointment(pid, old_date, new_date)
                print(result)
            except ValueError:
                print("Try again.\n")

        case "7":
            print("Get Appointment")
            pid = input("Enter Patient ID: ").strip()
            result = medical_sys.get_appointment(pid)
            print(result)

        case "8":
            print("Find Doctor Record")
            did = input("Enter Doctor ID: ").strip()
            try:
                result = medical_sys.find_doctor_record(did)
                print(result)
            except ValueError:
                print("Try again.\n")


        case "9":
            print("Find Patient Record")
            pid = input("Enter Patient ID: ").strip()
            try:
                result = medical_sys.find_patient_record(pid)
                print(result)
            except ValueError:
                print("Try again.\n")


        case _:
            print("Invalid option. Please try again.")








# medical_system = MedicalSystem()
# pat_me = Patient('oni', '10/05/2000', 'chest pain', 'Cardiology', {'phone number': '1234567809', 'email': 'lizzbet110@gmail.com', 'home address': '12 Broad str'})
# pat = Patient('oni', '10/05/2000', 'chest pain', 'Cardiology', {'phone number': '1234567809', 'email': 'lizzbet110@gmail.com', 'home address': '12 Broad str'})
# medical_system.add_patient(pat)
# medical_system.add_patient(pat_me)
# dr_zeus = Doctor('Dr. Ola', "Cardiology", {'phone number': '1234567809', 'email': 'lizzbet110@gmail.com', 'home address': '12 Broad str'})
# medical_system.add_doctor(dr_zeus)
# print(str(dr_zeus))
# print(str(pat_me))
# print(str(pat))



 # appointment_day_length = 3
                    # today = datetime.today()
                    # appointment_date = today + timedelta(days=random.randint(1, appointment_day_length))
                    # hour = random.randint(9, 15)
                    # min = random.randint(0, 59)
                    # appointment_d_t = appointment_date.replace(hour=hour, minute=min, second=0, microsecond=0)
                    # appointment_d_t = appointment_d_t.strftime('%d/%m/%Y %H:%M %p')
                    # medical_sys.assign_doctor_to_patient(patient, appointment_d_t)