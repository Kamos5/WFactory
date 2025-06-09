from os import system, name

import keyboard

class GameState():

    def __init__(self):

        self.MONTHS = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
        self.YEARS = ["1939", "1940", "1941", "1942", "1943", "1944", "1945"]
        self.MAIN_CITY_NAME = ["Poznań", "Posen"]
        self.COUNTRY_NAME = ["Polska", "Polen", "German Reich"]

        self.month_staring_counter = 4
        self.year_starting_counter = 0
        self.month_ending_counter = 4
        self.year_ending_counter = 6
        self.is_last_month = False
        self.current_month = self.month_staring_counter
        self.current_year = self.year_starting_counter
        self.city_name_flag = 0
        self.country_name_flag = 0

    def get_current_month_value(self):
        return self.MONTHS[self.current_month]

    def get_current_year_value(self):
        return self.YEARS[self.current_year]

    def get_city_name(self):
        return self.MAIN_CITY_NAME[self.city_name_flag]

    def get_country_name(self):
        return self.COUNTRY_NAME[self.country_name_flag]

gameState = GameState()
def main():
    while not gameState.is_last_month:
        printResources()
        printUIOptions()
        clear()
    return

def printResources():

    print(f'{gameState.get_current_month_value()} {gameState.get_current_year_value()} {gameState.get_city_name()} {gameState.get_country_name() }')
    print("Cash: 10000 PLN")
    print("Employment: 1000/1000")
    print("Workers: Polish <780> (78%) German <20> (2%) Jewish <200> (20%)")
    print("Stockpiled: 5000")
    print("Last month production: 1000")
    print("Polish support: 80")
    print("German support: -10")

    return

def printUIOptions():
    print()
    print("--Press Space to go to the next month--")
    wait_key()
    increase_month()












def wait_key():

    keyboard.wait('space')

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




