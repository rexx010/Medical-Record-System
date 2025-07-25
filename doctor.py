
class Doctor:
    def __init__(self, doctor_id, name, specialisation, contact_info: dict):
        self.set_id(doctor_id)
        self.set_name(name)
        self.set_specialisation(specialisation)
        self.set_contact_info(contact_info)

    def get_doctor_id(self):
        return self.doctor_id

    def set_id(self, doctor_id):
        if not doctor_id:
            raise ValueError("ID be empty")
        self.doctor_id = doctor_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

    def get_specialisation(self):
        return self.specialisation

    def set_specialisation(self, specialisation):
        if not specialisation:
            raise ValueError("Specialisation cannot be empty")
        self.specialisation = specialisation


    def get_contact_info(self):
        return self.contact_info

    def set_contact_info(self, contact_info):
        self.contact_info = contact_info
