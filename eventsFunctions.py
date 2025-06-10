import json

import events

def loadEvents():

    f = open('events.json')

    # returns JSON object as a dictionary
    data = json.load(f)

    # Iterating through the json list
    for i in data:
        print(i)