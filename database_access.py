# defines database access layer

from database_api import DatabaseApi
from models import Employee, Hospital, Room
import json


def getEmployeesInRoom(hospital_id, room_id) -> {}:
    try:
        db = DatabaseApi()
        employee_ids = db.get_employee_ids_in_room(hospital_id, room_id)
        employees = db.get_employees_by_ids(employee_ids)
        employeeObjects = []
        for employee in employees:
            newEmployee = Employee(employee[0], employee[1], employee[2], employee[3], employee[4])
            employeeObjects.append(newEmployee.to_dict())
    except Exception as e:
        print(e)
    finally:
        db.__del__()
        return json.dumps(employeeObjects)

def getHospitals() -> {}:
    try:
        db = DatabaseApi()
        hospitals = db.get_hospitals()
        hospitalObjects = []
        for hospital in hospitals:
            newHospital = Hospital(hospital[0], hospital[1], hospital[2])
            hospitalObjects.append(newHospital.to_dict())
    except Exception as e:
        print(e)
    finally:
        db.__del__()
        return json.dumps(hospitalObjects)

def getInformationForRooms(hospital_id) -> {}:
    try:
        db = DatabaseApi()
        rooms = db.get_rooms_for_hospital(hospital_id)
        room_id_to_rooms = {}
        for room in rooms:
            room_id_to_rooms[room[0]] = room
        room_id_to_num_employees = db.get_num_employees_per_room(hospital_id, room_id_to_rooms.keys())
        room_objects = []
        for room in rooms:
            room_object = Room(room[0], room[1], room[2], room[3], room_id_to_num_employees[room[0]])
            room_objects.append(room_object.to_dict())
    except Exception as e:
        print(e)
    finally:
        db.__del__()
        return json.dumps(room_objects)

def getRoomsInHospital(hospital_id) -> {}:
    try:
        db = DatabaseApi()
        rooms = db.get_rooms_for_hospital(hospital_id)
        room_objects = []
        for room in rooms:
            room_object = Room(room[0], room[1], room[2], room[3])
            room_objects.append(room_object.to_dict())
    except Exception as e:
        print(e)
    finally:
        db.__del__()
        return json.dumps(room_objects)