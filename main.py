from os import system, name

import keyboard

class GameState():

    def __init__(self):

        self.MONTHS = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
        self.YEARS = ["1939", "1940", "1941", "1942", "1943", "1944", "1945"]
        self.MAIN_CITY_NAME = ["Poznań", "Posen"]
        self.COUNTRY_NAME = ["Polska", "Polen", "German Reich"]
        self.CURRENCY = ["zł", "rm"]
        #polish, german, jews
        self.EMPLOYED = [780, 20, 200]
        self.EMPLOYED_NAMES = ['Polish', 'German', 'Jews']

        self.month_staring_counter = 4
        self.year_starting_counter = 0
        self.month_ending_counter = 4
        self.year_ending_counter = 6
        self.is_last_month = False
        self.current_month = self.month_staring_counter
        self.current_year = self.year_starting_counter
        self.city_name_flag = 0
        self.country_name_flag = 0
        self.personal_cash = 10000
        self.currency_flag = 0
        self.switched_currency = False
        self.max_employment = 1000
        self.employed = 0
        self.weapons_stockpiled = 5000
        self.last_month_weapons_prod = 1000
        self.polish_support = 80
        self.german_support = -20

    def get_current_month_value(self):
        return self.MONTHS[self.current_month]

    def get_current_year_value(self):
        return self.YEARS[self.current_year]

    def get_city_name(self):
        return self.MAIN_CITY_NAME[self.city_name_flag]

    def get_country_name(self):
        return self.COUNTRY_NAME[self.country_name_flag]

    def get_currency_name(self):
        return self.CURRENCY[self.currency_flag]

    def get_personal_cash(self):
        return self.personal_cash

    def convert_from_zl_to_rm(self):
        self.personal_cash = self.personal_cash // 2
        self.currency_flag = 1

    def get_switched_currency(self):
        return self.switched_currency

    def switch_currency(self):
        self.switched_currency = not self.switched_currency
        self.convert_from_zl_to_rm()

    def get_max_employment(self):
        return self.max_employment

    def calculate_employed(self):
        self.employed = sum(self.EMPLOYED)

    def get_employed(self):
        self.calculate_employed()
        return self.employed

    def get_employed_group_name(self, index):
        return self.EMPLOYED_NAMES[index]

    def get_employed_group_number(self, index):
        return self.EMPLOYED[index]

    def get_perc_group_of_employed(self, index):
        return self.get_employed_group_number(index) / self.get_employed() * 100

    def get_weapons_stockpiled(self):
        return self.weapons_stockpiled

    def get_last_month_weapons_prod(self):
        return self.last_month_weapons_prod

    def get_polish_support(self):
        return self.polish_support

    def get_german_support(self):
        return self.german_support

    def increase_weapons_stockpiled(self):
        self.weapons_stockpiled += self.get_last_month_weapons_prod()

gameState = GameState()
def main():
    while not gameState.is_last_month:
        print_resources()
        print_ui_options()
        process_time()
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
    increase_month()






def process_time():

    if gameState.current_month == 8 and gameState.current_year == 0:
        gameState.switch_currency()

    gameState.increase_weapons_stockpiled()

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




