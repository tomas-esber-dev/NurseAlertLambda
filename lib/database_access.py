# defines database access layer

from database.database_api import DatabaseApi


def getEmployeesInRoom(hospital_id, room_id) -> {}:
    try:
        db = DatabaseApi()
        employee_ids = db.get_employee_ids_in_room(hospital_id, room_id)
        employees = db.get_employees_by_ids(employee_ids)
    except Exception as e:
        print(e)
    finally:
        db.__del__()
        return employees

def getHospitals() -> {}:
    try:
        db = DatabaseApi()
        hospitals = db.get_hospitals()
    except Exception as e:
        print(e)
    finally:
        db.__del__()
        return hospitals

def getInformationForRooms(hospital_id) -> {}:
    try:
        db = DatabaseApi()
        rooms = db.get_rooms_for_hospital(hospital_id)
        room_id_to_rooms = {}
        for room in rooms:
            room_id_to_rooms[room[0]] = room
        room_id_to_num_employees = db.get_num_employees_per_room(hospital_id, room_id_to_rooms.keys())
        room_info = []
        for room_id in room_id_to_rooms.keys():
            current_room = room_id_to_rooms[room_id]
            room_info.append({
                "id": current_room[0],
                "room_name": current_room[1],
                "hospital_id": current_room[2],
                "division": current_room[3],
                "num_employees": room_id_to_num_employees[room_id]
            })
    except Exception as e:
        print(e)
    finally:
        db.__del__()
        return room_info

def getRoomsInHospital(hospital_id) -> {}:
    try:
        db = DatabaseApi()
        rooms = db.get_rooms_for_hospital(hospital_id)
    except Exception as e:
        print(e)
    finally:
        db.__del__()
        return rooms

# getInformationForRooms(1)
res = getRoomsInHospital(1)
print(res)
