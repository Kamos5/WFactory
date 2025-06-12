import json
import operator

import events as ev

def loadEvents():

    f = open('events.json')

    # returns JSON object as a dictionary
    data = json.load(f)

    return mapToClass(data)

def mapToClass(data):

    events_list = []

    for i in data:
        events = ev.Events()
        events.id = i["id"]
        events.title = i["title"]
        events.description = i["description"]
        events.init_month = i["init_month"]
        events.init_year = i["init_year"]
        events.init_flag = i["init_flag"]
        events.option_1 = i["option_1"]
        events.option_2 = i["option_2"]
        events.option_3 = i["option_3"]
        events.effects_from_option_1 = i["effects_from_option_1"]
        events.effects_from_option_2 = i["effects_from_option_2"]
        events.effects_from_option_3 = i["effects_from_option_3"]
        events_list.append(events)

    return events_list

def sortEvents(events_list):

    s = sorted(events_list, key=operator.attrgetter('init_year','init_month'), reverse=False)

    return s
