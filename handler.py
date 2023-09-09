import logging
import boto3

def handle_request(event, context):
    return send_message()


def send_message():
    sns_client = boto3.client('sns')
    response = sns_client.publish(PhoneNumber='+33680866163', 
                                    Message='Python Hello!',
                                    Subject='Message from Tomas')
    return response
