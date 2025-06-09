from os import system, name
import gameState as gameState
import keyboard


gameState = gameState.GameState()
def main():
    while not gameState.is_last_month:
        print_resources()
        print_ui_options()
        process_time()
        increase_month()
        clear()
    return

def print_resources():

    print(f'{gameState.get_current_month_value()} {gameState.get_current_year_value()} {gameState.get_city_name()} {gameState.get_country_name() }')
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




