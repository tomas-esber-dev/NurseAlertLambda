import boto3

# determine the urgency of a request using LLM
def findUrgency(event, context):
    return 0

# consult database to find phone number and name for an available employee
def send_message(urgency):
    sns_client = boto3.client('sns')
    response = sns_client.publish(PhoneNumber='+33680866163',
                                  Message='A patient is requesting you with {urgency} urgency',
                                  Subject='Message from Patient')
    return response