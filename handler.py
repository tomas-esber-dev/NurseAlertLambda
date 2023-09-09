from lib import sender

def handle_request(event, context):
    return sender.send_message()
