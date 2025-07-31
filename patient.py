from datetime import datetime

class Patient:
    patient_id_counter = 0

    def __init__(self, name: str, dob: str, problem: str, speciality_needed: str ,contact_info: dict):
        self.id = self.__create_id()
        self.name = name
        self.dob = dob
        self.problem = problem
        self.speciality_needed = speciality_needed
        self.contact_info = contact_info

    @classmethod
    def __create_id(cls):
        cls.patient_id_counter += 1
        return f"PAT{cls.patient_id_counter}"

    @property
    def get_id(self):
        return self.id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        self.__dob = dob

    @property
    def problem(self):
        return self.__problem

    @problem.setter
    def problem(self, problem):
        self.__problem = problem

    @property
    def speciality_needed(self):
        return self.__speciality_needed

    @speciality_needed.setter
    def speciality_needed(self, speciality_needed):
        self.__speciality_needed = speciality_needed

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        self.__contact_info = contact_info

    def __str__(self):
        return (f"Name: Patient {self.name}.\n"
                f"Date of birth: {self.dob}.\n"
                f"Contact: {self.contact_info}\n"
                f"Battling with {self.problem},\n"
                f"Needs a doctor from the {self.speciality_needed} department\n"
                f"Assigned ID: {self.get_id}")