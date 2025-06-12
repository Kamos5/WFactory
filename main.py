from os import system, name
from random import randint

from inputimeout import inputimeout, TimeoutOccurred

import gameState as gameState
import eventsFunctions as EF
import keyboard


gameState = gameState.GameState()
def main():

    gameState.EVENT_LIST = EF.sortEvents(EF.loadEvents())
    while not gameState.is_last_month:
        gameState.clear_events_to_run()
        check_for_events()
        launch_events()
        print_resources()
        print_ui_options()
        process_time()
        increase_month()
        clear()
    return

def print_resources():

    print(f'{gameState.get_current_month_value()} {gameState.get_current_year_value()} {gameState.get_city_name()} {gameState.get_country_name()}')
    print(f'Cash: {gameState.get_personal_cash()} {gameState.get_currency_name()}')
    print(f'Employment: {gameState.get_employed()}/{gameState.get_max_employment()}')
    print(f'Workers: {gameState.get_employed_group_name(0)} <{gameState.get_employed_group_number(0)}> ({gameState.get_perc_group_of_employed(0)}%) {gameState.get_employed_group_name(1)} <{gameState.get_employed_group_number(1)}> ({gameState.get_perc_group_of_employed(1)}%) {gameState.get_employed_group_name(2)} <{gameState.get_employed_group_number(2)}> ({gameState.get_perc_group_of_employed(2)}%)')
    print(f'Weapons stockpiled: {gameState.get_weapons_stockpiled()}')
    print(f'Last month production: {gameState.get_last_month_weapons_prod()}')
    print(f'Polish support: {gameState.get_polish_support()}')
    print(f'German support: {gameState.get_german_support()}')

    return

def print_ui_options():
    print()
    print("--Press Space to go to the next month--")
    wait_key()
    # wait_key2()


def check_for_events():

    if len(gameState.get_events()) > 0:
        for event in gameState.get_events():
            if event.get_init_month() == gameState.get_current_month_index() and event.get_init_year() == gameState.get_current_year_value():
                gameState.append_events_to_run(event)


def launch_events():

    for event in gameState.EVENT_TO_RUN_LIST:
        process_event(event)
        # clear()

def process_event(event):

    print("#################EVENT#######################")
    print(event.title)
    print(event.description)
    if len(event.option_1) > 0:
        suffix = ''
        if len(event.effects_from_option_1) > 0:
            for effect in event.effects_from_option_1:
                suffix += f' ({effect[0]}: {effect[1]})'
        print("1. " + event.option_1 + suffix)
    if len(event.option_2) > 0:
        suffix = ''
        if len(event.effects_from_option_2) > 0:
            for effect in event.effects_from_option_2:
                suffix += f' ({effect[0]}: {effect[1]})'
        print("2. " + event.option_2 + suffix)
    if len(event.option_3) > 0:
        suffix = ''
        if len(event.effects_from_option_3) > 0:
            for effect in event.effects_from_option_3:
                suffix += f' ({effect[0]}: {effect[1]})'
        print("3. " + event.option_3 + suffix)

    try:
        c = inputimeout(prompt='<You have 30 sec to pick a choice or random one with be picked>', timeout=30)
    except TimeoutOccurred:
        c = randint(1, 3)
    if c.strip().isdecimal():
        option = int(c.strip())
        match option:
            case 1:
                process_event_outcome(event, 1)
            case 2:
                process_event_outcome(event, 2)
            case 3:
                process_event_outcome(event, 3)


    return


def process_event_outcome(event, choice):

    return
def process_time():

    # 09/1939
    if gameState.current_month == 8 and gameState.current_year == 0:
        gameState.switch_currency()
        gameState.change_employed_workers_number(2, - gameState.get_employed_group_number(2))
    # 10/1939
    if gameState.current_month == 9 and gameState.current_year == 0:
        gameState.switch_countries()

    # 03/1945
    if gameState.current_month == 2 and gameState.current_year == 6:
        gameState.switch_countries()
        gameState.switch_currency()

    gameState.process_production()
    gameState.monthly_personal_profit()
    gameState.increase_weapons_stockpiled()

def wait_key():

    keyboard.wait('space')

def wait_key2():
    keyboard.wait('enter')
def increase_month():

    gameState.current_month += 1
    if gameState.current_month == 12:
        gameState.current_year += 1
        gameState.current_month = 0
    if gameState.current_year == 6 and gameState.current_month == 4:
        gameState.is_last_month = True


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

clear()
main()




