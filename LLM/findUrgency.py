import json
import numpy as np
from collections import defaultdict
import os
import openai
# Need python interpreter 3.10.12 for openai import to work
openai.api_key = "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"


def findUrgency(request):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": "A classifying chatbot educated on healthcare."},
            {"role": "user", "content": f"Classify the severity of the patient request with a one word response of 'high', 'medium', or 'low': {request}"}
        ]
    )
    print(completion.choices[0].message['content'])


def main():
    findUrgency("I'm having trouble breathing")
    findUrgency("My throat is very sore")
    findUrgency("I have to pee")


if __name__ == "__main__":
    main()
