from LLM.findUrgency import findUrgency
from database_access import getEmployeesInRoom
import boto3
import json

# consult database to find phone number and name for an available employee
def request_help(input, hospital_id, room_id):
    urgency = findUrgency(input)
    employees = json.loads(getEmployeesInRoom(hospital_id, room_id))
    employeeToContact = None

    if urgency == "high":
        employees.sort(key=lambda emp: emp["priority"])
        employeeToContact = employees[len(employees) -1]
    elif urgency == "low":
        employees.sort(key=lambda emp: emp["priority"])
        employeeToContact = employees[0]
    else:
        employees.sort(key=lambda emp: abs(emp["priority"] - 3))
        employeeToContact = employees[0]
    if employeeToContact:
        
        print("Phone number", employeeToContact["number"])
        print('Hello {}! A patient is requesting you with {} urgency'.format(employeeToContact["name"], urgency))
        sns_client = boto3.client('sns', region_name='us-east-1')
        response = sns_client.publish(PhoneNumber='+{}'.format(employeeToContact["number"]),
                                    Message='Hello {}! A patient is requesting you with {} urgency'.format(employeeToContact["name"], urgency),
                                    Subject='Message from Patient')
    return response

print(request_help("I am coughing", 1, 1))