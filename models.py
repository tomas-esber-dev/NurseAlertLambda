class Hospital:
    def __init__(self, hospital_id, hospital_name, image_url):
        self.hospital_id = hospital_id
        self.hospital_name = hospital_name
        self.image_url = image_url
    def to_dict(self):
        return {
            "hospital_id": self.hospital_id,
            "hospital_name": self.hospital_name,
            "image_url": self.image_url
        }

class Employee:
    def __init__(self, employee_id, name, number, priority, role):
        self.employee_id = employee_id
        self.name = name
        self.number = number
        self.priority = priority
        self.role = role
    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "number": self.number,
            "priority": self.priority,
            "role": self.role
        }

class Room:
    def __init__(self, room_id, room_name, hospital_id, division, num_employees=None):
        self.room_id = room_id
        self.room_name = room_name
        self.hospital_id = hospital_id
        self.division = division
        self.num_employees = num_employees
    def to_dict(self):
        return {
            "room_id": self.room_id,
            "room_name": self.room_name,
            "hospital_id": self.hospital_id,
            "division": self.division,
            "num_employees": self.num_employees
        }