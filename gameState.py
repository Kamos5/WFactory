class GameState():

    def __init__(self):

        self.MONTHS = ["JANUARY",    "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
        self.YEARS = ["1939", "1940", "1941", "1942", "1943", "1944", "1945"]
        self.MAIN_CITY_NAME = ["Poznań", "Posen"]
        self.COUNTRY_NAME = ["Polska", "German Reich"]
        self.CURRENCY = ["złotych", "reichmarks"]
        #polish, german, jews
        self.EMPLOYED = [780, 20, 200]
        self.EMPLOYED_NAMES = ['Polish', 'German', 'Jews']
        self.EMPLOYED_PRODUCTIVITY = [1, 1.2, 1]

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
        self.max_employment = 1000
        self.employed = 0
        self.weapons_stockpiled = 5000
        self.personal_price_per_weapon = 0.24
        self.last_month_weapons_prod = 0
        self.polish_default_support = 50
        self.polish_support = 50
        self.german_default_support = -20
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

    def change_person_cash(self, value):
        self.personal_cash += value

    def monthly_personal_profit(self):
        self.change_person_cash(int(round(self.get_last_month_weapons_prod() * self.personal_price_per_weapon, 0)))

    def convert_from_zl_to_rm(self):
        if self.currency_flag == 0:
            self.personal_cash = self.personal_cash // 2
            self.change_personal_price_profit(self.personal_price_per_weapon / 2)
        else:
            self.personal_cash = self.personal_cash * 2
            self.change_personal_price_profit(self.personal_price_per_weapon * 2)
        self.currency_flag ^= 1

    def switch_currency(self):
        self.convert_from_zl_to_rm()

    def switch_countries(self):
        self.city_name_flag ^= 1
        self.country_name_flag ^= 1

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

    def get_employed_productivity(self, index):
        return self.EMPLOYED_PRODUCTIVITY[index]

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

    def process_production(self):
        self.last_month_weapons_prod = self.get_employed_group_number(0) * self.get_employed_productivity(0) + self.get_employed_group_number(1) * self.get_employed_productivity(1) + self.get_employed_group_number(2) * self.get_employed_productivity(2)

    def increase_weapons_stockpiled(self):
        self.weapons_stockpiled += self.get_last_month_weapons_prod()

    def change_employed_workers_number(self, index, number):
        self.EMPLOYED[index] += number

    def change_personal_price_profit(self, newValue):
        self.personal_price_per_weapon = newValue