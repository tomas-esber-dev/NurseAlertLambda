import sender, database_access

# defines the methods mapped to lambda and accessed through API gateway endpoint.

def handle_send_request(event, context):
    return {
        'statusCode': 200,
        'body': sender.send_message(event["queryStringParameters"]["urgency"])
    }

def handle_getEmployeesInRoom_request(event, context):
    return {
        'statusCode': 200,
        'body': database_access.getEmployeesInRoom(event["queryStringParameters"]["hospital_id"], event["queryStringParameters"]["room_id"])
    }

def handle_getHospitals_request(event, context):
    return {
        'statusCode': 200,
        'body': database_access.getHospitals()
    }

def handle_getInformationForRooms_request(event, context):
    return {
        'statusCode': 200,
        'body': database_access.getInformationForRooms(event["queryStringParameters"]["hospital_id"])
    }

def handle_getRoomsInHospital_request(event, context):
    return {
        'statusCode': 200,
        'body': database_access.getRoomsInHospital(event["queryStringParameters"]["hospital_id"])
    }