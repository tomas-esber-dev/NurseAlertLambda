from lib import sender, database_access

# defines the methods mapped to lambda and accessed by API gateway endpoint.

def handle_send_request(event, context):
    return sender.send_message("")

def handle_getEmployeesByIds_request(event, context):
    return database_access.getEmployeesByIds("")

def handle_getEmployeesInRoom_request(event, context):
    return database_access.getEmployeesInRoom("", "")

def handle_getHospitals_request(event, context):
    return database_access.getHospitals()

def handle_getNumberOfEmployeesInRooms_request(event, context):
    return database_access.getNumberOfEmployeesInRooms("")

def handle_getRoomsInHospital_request(event, context):
    return database_access.getRoomsInHospital("")