import re
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
press 0 to Exit
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
                    name = input("Enter Doctor's full Name: ")
                    while True:
                        if not isinstance(name, str) or not name.strip():
                            print("Invalid name. Please enter a valid name.")
                            name = input("Enter Doctor's full Name: ")
                        else:
                            break
                    specialisation = input("Enter Doctor's Specialisation: ")
                    while True:
                        if not isinstance(specialisation, str) or not specialisation.strip():
                            print("Invalid specialisation. Please enter a valid specialisation.")
                            specialisation = input("Enter Doctor's Specialisation: ")
                        else:
                            break
                    phone = input("Enter Doctor's Phone Number which must be 11 digit and it must either begin with(070,080,081,090,071,091): ")
                    while True:
                        if not re.match(r"^(070|080|081|090|071|091)[0-9]{8}$", phone):
                            print("Invalid phone number format. Please try again.")
                            phone = input("Enter Doctor's Phone Number: ")
                        else:
                            break
                    email = input("Enter Doctor's Email Address: ").strip()
                    while True:
                        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$", email):
                            print("Invalid email format. Please try again.")
                            email = input("Enter Doctor's Email Address: ").strip()
                        else:
                            break
                    address = input("Enter Doctor's Address: ")
                    while True:
                        if not isinstance(address, str) or not address.strip():
                            print("Invalid address. Please enter a valid address.")
                            address = input("Enter Doctor's Address: ")
                        else:
                            break
                    contact_info["phone"] = phone
                    contact_info["email"] = email
                    contact_info["address"] = address
                    doctor = Doctor(name=name, specialisation=specialisation, contact_info=contact_info)
                    medical_sys.add_doctor(doctor)
                    print(doctor)
                    break
                except ValueError:
                    print("invalid input... Try again.\n")
        case "2":
            print("Add Patient")
            contact_info = {}
            while True:
                p_name = input("Enter Patient's Full Name: ")
                if isinstance(p_name, str) and p_name.strip():
                    break
                print("Invalid name. Please enter a valid name.")

            while True:
                date_of_birth = input("Enter Patient's Date of Birth(DD/MM/YYYY): ").strip()
                try:
                    date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y %H:%M')
                    dob = date_of_birth.strftime('%d/%m/%Y %H:%M')
                    break
                except ValueError:
                    print("Date of birth must be in DD/MM/YYYY format(eg, 10/05/2000)")
            while True:
                problem = input("Enter the patient problem: ")
                if isinstance(problem, str) and problem.strip():
                    break
                print("Invalid problem. Please enter a valid problem.")

            while True:
                specialty_needed = input("Enter the patient specialty needed: ")
                if isinstance(specialty_needed, str) and specialty_needed.strip():
                    break
                print("Invalid speciality. Please enter a valid speciality.")

            while True:
                phone = input("Enter Patient's Phone Number which must be 11 digit and it must either begin with(070,080,081,090,071,091): ")
                if re.match(r"^(070|080|081|090|071|091)[0-9]{8}$", phone):
                    break
                print("Invalid phone number format. Please try again.")


            while True:
                email = input("Enter Patient's Email Address: ")
                if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$", email):
                    break
                print("Invalid email format. Please try again.")

            while True:
                address = input("Enter Patient's Address: ")
                if isinstance(address, str) and address.strip():
                    break
                print("Invalid address. Please enter a valid address.")

            contact_info["phone"] = phone
            contact_info["email"] = email
            contact_info["address"] = address

            try:
                new_patient = Patient(name=p_name, dob=dob, problem=problem, speciality_needed=specialty_needed, contact_info=contact_info)
                medical_sys.add_patient(new_patient)
                patient_list[new_patient.get_id] = new_patient
                print(new_patient)
            except ValueError:
                print("Oga...go back and enter the correct details.\n")


        case "3":
            print("Create Appointment")
            while True:
                try:
                    pid = input("Enter Patient ID: ").strip()
                    while True:
                        try:
                            schedule_date = input("Enter Appointment date in DD/MM/YYYY HH:MM format(eg, 10/05/2000 03:00): ").strip()
                            schedule_date = datetime.strptime(schedule_date, '%d/%m/%Y %H:%M')
                            if schedule_date < datetime.now():
                                raise ValueError("Appointment date cannot be in the past")
                            else:
                                schedule_date = schedule_date.strftime('%d/%m/%Y %H:%M')
                                break
                        except ValueError:
                            raise ValueError("Appointment date must be in DD/MM/YYYY HH:MM format(eg, 10/05/2000 03:00)")
                    patient = patient_list.get(pid)
                    if patient:
                        result = medical_sys.assign_doctor_to_patient(patient, schedule_date)
                        print(result)
                        break
                except ValueError:
                    print("Try again.\n")

        case "4":
            print("View all Appointments")
            medical_sys.view_all_appointments()

        case "5":
            print("Cancel Appointment")
            while True:
                try:
                    pid = input("Enter Patient ID: ").strip()
                    date = input("Enter Appointment date in DD/MM/YYYY HH:MM format: ").strip()
                    datetime.strptime(date, "%d/%m/%Y %H:%M")
                    result = medical_sys.cancel_appointment(pid, date)
                    print(result)
                    break
                except ValueError:
                    print("Try again.\n")

        case "6":
            print("Reschedule Appointment")
            while True:
                try:
                    pid = input("Enter Patient ID: ").strip()
                    old_date = input("Enter old Appointment date in DD/MM/YYYY HH:MM format: ").strip()
                    datetime.strptime(old_date, "%d/%m/%Y %H:%M")
                    new_date = input("Enter new Appointment date in DD/MM/YYYY HH:MM format: ").strip()
                    datetime.strptime(new_date, "%d/%m/%Y %H:%M")
                    result = medical_sys.reschedule_appointment(pid, old_date, new_date)
                    print(result)
                    break
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
            result = medical_sys.find_doctor_record(did)
            print(result)


        case "9":
            print("Find Patient Record")
            pid = input("Enter Patient ID: ").strip()
            result = medical_sys.find_patient_record(pid)
            print(result)

        case "0":
            print("Exiting the Medical System. Goodbye!")
            break


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